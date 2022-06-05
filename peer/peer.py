import datetime
import random
import string
import time
from concurrent import futures
import logging
import google

import const
import koloocheh_pb2_grpc
from const import Const
from koloocheh_pb2_grpc import PeerToPeerServicer
from koloocheh_pb2 import Address, File, SearchMessage, SearchResponse
import grpc
from typing import List, Set, Dict


class QueryInfo:
    def __init__(self, initiated_at):
        self.initiated_at = initiated_at
        self.responding_peers: List[Address] = []


class Peer(PeerToPeerServicer):

    def __init__(self, address: Address):
        self.address = address
        self.neighbours: List[Address] = []
        self.files: List[File] = []

        self.query_mark: Set[str] = set()
        self.query_files: Dict[str, List[Address]] = dict()
        self.queries_initiated: Dict[str, datetime.datetime] = dict()
        self.id_to_filename: Dict[str, str] = dict()

        self.logger = logging.getLogger(__name__)

    def FoundFile(self, request, context):
        address: Address = request.addr
        identifier: str = request.identifier
        self.logger.info(f"Query with id='{identifier}' found requested file at ({address.ip},{address.port})")

        if identifier in self.query_files:
            self.query_files[identifier].append(address)
        else:
            self.query_files[identifier] = [address]
        return google.protobuf.empty_pb2.Empty()

    def SearchFile(self, request: SearchMessage, context):
        sender, name, identifier = (
            request.addr,
            request.fileName,
            request.identifier,
        )

        if identifier in self.query_mark:
            return google.protobuf.empty_pb2.Empty()

        self.query_mark.add(identifier)

        found = False
        for file in self.files:
            if file.name == name:
                found = True

        if found:
            file_requester_address: Address = request.addr
            with grpc.insecure_channel(f'localhost:{file_requester_address.port}') as channel:
                stub = koloocheh_pb2_grpc.PeerToPeerStub(channel)
                stub.FoundFile(
                    SearchResponse(
                        addr=self.address,
                        identifier=request.identifier
                    )
                )
        else:
            self.search(name, identifier)

        return google.protobuf.empty_pb2.Empty()

    def upload(self, name: str, data: str):
        file = File(
            name=name,
            data=data
        )
        self.files.append(file)

    def print_files(self):
        return self.files

    @staticmethod
    def gen_random_identifier():
        return ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=Const.Peer.IDENTIFIER_LENGTH,
            )
        )

    def initiate_search(self, name: str):
        identifier = self.gen_random_identifier()

        self.query_mark.add(identifier)
        self.queries_initiated[identifier] = datetime.datetime.now()

        self.id_to_filename[identifier] = name

        self.search(name, identifier)

    def search(self, name: str, identifier: str):
        """rpc to all neighbours"""

        if identifier not in self.query_mark:
            self.query_mark.add(identifier)
        self.logger.info(f'Neighbours before search: {self.neighbours}')
        for neighbour_addr in self.neighbours:
            self._search(identifier, name, neighbour_addr)

    def _search(self, identifier, name, neighbour_addr):
        with grpc.insecure_channel(f'localhost:{neighbour_addr.port}') as channel:
            stub = koloocheh_pb2_grpc.PeerToPeerStub(channel)

            stub.SearchFile(
                SearchMessage(
                    addr=self.address,
                    fileName=name,
                    identifier=identifier,
                )
            )

    def add_neighbour(self, address: Address):
        self.neighbours.append(address)

    def advertise_to_master(self):
        with grpc.insecure_channel(f'localhost:{const.Const.MASTER_ADDRESS.port}') as channel:
            stub = koloocheh_pb2_grpc.PeerMasterStub(channel)
            stub.PeerJoined(self.address)

    def get_neighbours(self):
        while True:
            time.sleep(Const.Peer.GET_NEIGHBOUR_RATE)
            with grpc.insecure_channel(
                    f'localhost:{const.Const.MASTER_ADDRESS.port}'
            ) as channel:
                stub = koloocheh_pb2_grpc.PeerMasterStub(channel)
                self.neighbours = stub.GetNeighbours(self.address).neighbours
                # self.logger.info(f'Neighbours received from master: \n{self.neighbours}')

    def check_query_results(self):
        """Check status for each query"""
        while True:
            time.sleep(Const.Peer.QUERY_TTL * 1.5)

            queries_expired = []
            for query in self.queries_initiated:
                if (datetime.datetime.now() - self.queries_initiated[query]).total_seconds() > \
                        Const.Peer.QUERY_TTL:
                    self.logger.info(f'query (id={query}, filename={self.id_to_filename[query]}) expired')
                    queries_expired.append(query)

            for query in queries_expired:
                self._remove_query(query)

    def _remove_query(self, query: str):
        self.queries_initiated.pop(query, None)
        self.query_mark.remove(query)
        self.query_files.pop(query, None)


def serve(peer: Peer):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    koloocheh_pb2_grpc.add_PeerToPeerServicer_to_server(
        peer, server)
    server.add_insecure_port(f'localhost:{peer.address.port}')
    server.start()
    server.wait_for_termination()
