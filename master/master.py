import logging
import random
import time
import google
import grpc
import koloocheh_pb2_grpc

from concurrent import futures
from threading import Thread
from typing import List, Dict, Tuple
from const import Const
from koloocheh_pb2 import Address, NeighbourList
from koloocheh_pb2_grpc import PeerMasterServicer
from serializer import AddressTupleSerializer


class Master(PeerMasterServicer):

    def __init__(self, address: Address):
        self.address: Address = address
        self.prob_edge = 1
        self.network: Dict[
            Tuple[int, int],
            List[Tuple[int, int]]
        ] = dict()

        self.logger = logging.getLogger(__name__)

    def run(self):
        t = Thread(
            target=serve,
            args=(self,),
            daemon=True
        )
        t.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            exit(1)

    def PeerJoined(self, request, context):
        address: Tuple[int, int] = AddressTupleSerializer.to_tuple(request)
        self.network[address] = []

        self.logger.info(f"Peer with ip={request.ip} , port={request.port} joined Koloocheh!")

        for p in self.network:
            if p == address:
                continue
            if random.random() <= self.prob_edge:
                self.network[address].append(p)
                self.network[p].append(address)
                self.logger.info(f"Connection established between {address}, {p}")

        return google.protobuf.empty_pb2.Empty()

    def GetNeighbours(self, request, context):
        address = AddressTupleSerializer.to_tuple(request)

        return NeighbourList(
            neighbours=[
                AddressTupleSerializer.to_address(x)
                for x in self.network[address]
            ]
        )


def serve(master: Master):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    koloocheh_pb2_grpc.add_PeerMasterServicer_to_server(
        master, server)
    server.add_insecure_port(f'localhost:{Const.MASTER_ADDRESS.port}')
    server.start()
    server.wait_for_termination()
