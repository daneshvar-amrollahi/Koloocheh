import datetime
import logging
import random
import time
import google
import grpc

import const
import koloocheh_pb2_grpc
import datetime

from concurrent import futures
from threading import Thread, Lock
from typing import List, Dict, Tuple, Set
from const import Const
from koloocheh_pb2 import Address, NeighbourList
from koloocheh_pb2_grpc import PeerMasterServicer
from serializer import AddressTupleSerializer


class Master(PeerMasterServicer):

    def __init__(self, address: Address):
        self.address: Address = address
        self.prob_edge = 1
        self.network: Dict[Tuple[int, int], Set[Tuple[int, int]]] = dict()
        self.last_grpc_call: Dict[Tuple[int, int], datetime.datetime] = dict()
        self.logger = logging.getLogger(__name__)

    def run(self):
        thread_run = Thread(
            target=serve,
            args=(self,),
            daemon=True
        )
        thread_run.start()

        thread_check_liveness = Thread(
            target=self.check_liveness,
            args=(),
            daemon=True
        )
        thread_check_liveness.start()

        try:
            while True:
                self.handle_command()
        except KeyboardInterrupt:
            exit(1)

    def handle_command(self):
        command = input()
        if command == "show":
            self.print_graph()

    def check_liveness(self):
        dead_peers = []
        while True:
            time.sleep(Const.Peer.CHECK_LIVENESS_RATE)
            for address in self.network:
                now = datetime.datetime.now()
                if (now - self.last_grpc_call[address]).total_seconds() > const.Const.Peer.CHECK_LIVENESS_RATE:
                    self.logger.info(f"Peer with address ip={address[0]}, port={address[1]} is DEAD!")
                    dead_peers.append(address)

            for dead_peer in dead_peers:
                self._remove_peer_from_network(AddressTupleSerializer.to_address(dead_peer))

    def _remove_peer_from_network(self, address: Address):
        address = AddressTupleSerializer.to_tuple(address)
        neighbours = self.network.pop(address, set())
        for neighbour in neighbours:
            self.network[neighbour].remove(address)
        self.last_grpc_call.pop(address, None)

    def PeerJoined(self, request, context):
        address: Tuple[int, int] = AddressTupleSerializer.to_tuple(request)
        self.network[address] = set()
        self.logger.info(f"Peer with ip={request.ip} , port={request.port} joined Koloocheh!")
        self.logger.info(f"PeerJoined: network: {self.network}")
        self.last_grpc_call[address] = datetime.datetime.now()
        for p in self.network:
            if p == address:
                continue
            if random.random() <= self.prob_edge:
                self.network[address].add(p)
                self.network[p].add(address)
                self.logger.info(f"Connection established between {address}, {p}")

        return google.protobuf.empty_pb2.Empty()

    def GetNeighbours(self, request, context):
        address = AddressTupleSerializer.to_tuple(request)
        self.logger.info(f"GetNeighbours: network: {self.network}")
        self.last_grpc_call[address] = datetime.datetime.now()
        return NeighbourList(
            neighbours=[
                AddressTupleSerializer.to_address(x)
                for x in self.network[address]
            ]
        )

    def print_graph(self):
        for peer in self.network:
            print(f"{peer}: {self.network[peer]}")


def serve(master: Master):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    koloocheh_pb2_grpc.add_PeerMasterServicer_to_server(
        master, server)
    server.add_insecure_port(f'localhost:{Const.MASTER_ADDRESS.port}')
    server.start()
    server.wait_for_termination()
