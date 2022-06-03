import time
from concurrent import futures

import google
import nutellamd_pb2_grpc
from nutellamd_pb2 import Address
from nutellamd_pb2_grpc import PeerMasterServicer
from typing import List
import logging
import grpc
from const import Const
from threading import Thread

class Master(PeerMasterServicer):

    def __init__(self, address: Address):
        self.address: Address = address
        self.prob_edge = 1
        self.peers: List[Address] = []
        self.logger = logging.getLogger(__name__)

    def run(self):
        t = Thread(
            target=serve,
            args=(self,),
            daemon=True
        )
        t.start()

        try:
            while (True):
                time.sleep(1)
        except KeyboardInterrupt:
            exit(1)

    def PeerJoined(self, request, context):
        self.peers.append(request)
        self.logger.info(f"Peer with ip={request.ip} , port={request.port} joined NutellaMD!")
        return google.protobuf.empty_pb2.Empty()



def serve(master: Master):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    nutellamd_pb2_grpc.add_PeerMasterServicer_to_server(
        master, server)
    server.add_insecure_port(f'localhost:{Const.MASTER_ADDRESS.port}')
    server.start()
    server.wait_for_termination()
