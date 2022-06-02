import random
import string
from concurrent import futures

import google

import nutellamd_pb2_grpc
from nutellamd_pb2_grpc import PeerToPeerServicer
from nutellamd_pb2 import TestMessage, Address, File, SearchMessage, SearchResponse
import grpc
from typing import List, Set


class Peer(PeerToPeerServicer):

    def __init__(self, address: Address):
        self.address = address
        self.neighbours: List[Address] = []
        self.files: List[File] = []
        self.query_ids: Set[str] = set()

    def TestRpc(self, request, context):
        return TestMessage(
            text="NutellaMD"
        )

    def SearchFile(self, request: SearchMessage, context):
        # TODO: Add lock
        print(f'SearchFile called on {self.address.port}')
        sender, name, identifier = (
            request.addr,
            request.fileName,
            request.identifier,
        )

        if identifier in self.query_ids:
            return google.protobuf.empty_pb2.Empty()
        self.query_ids.add(identifier)

        found = False
        for file in self.files:
            if file.name == name:
                print(f"File found in ({self.address.ip},{self.address.port})")
                found = True

        if not found:
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
    def _get_random_identifier():
        LENGTH = 10
        return ''.join(
            (random.choice(string.ascii_lowercase) for x in range(LENGTH))
        )

    def search(self, name: str, identifier: str = None):
        """rpc to all neighbours"""
        print(f'search called in {self.address.port}')
        for neighbour_addr in self.neighbours:
            print(f'trying to search on {neighbour_addr.port}')
            self._search_on_neighbour(identifier, name, neighbour_addr)

        print("Client received")

    def _search_on_neighbour(self, identifier, name, neighbour_addr):
        with grpc.insecure_channel(f'localhost:{neighbour_addr.port}') as channel:
            stub = nutellamd_pb2_grpc.PeerToPeerStub(channel)
            message_id = identifier if identifier \
                else self._get_random_identifier()

            stub.SearchFile(
                SearchMessage(
                    addr=self.address,
                    fileName=name,
                    identifier=message_id,
                )
            )

    def add_neighbour(self, address: Address):
        self.neighbours.append(address)


def serve(peer: Peer):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    nutellamd_pb2_grpc.add_PeerToPeerServicer_to_server(
        peer, server)
    server.add_insecure_port(f'localhost:{peer.address.port}')
    server.start()
    server.wait_for_termination()
