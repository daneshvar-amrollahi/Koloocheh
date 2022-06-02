from concurrent import futures

import nutellamd_pb2_grpc
from nutellamd_pb2_grpc import PeerToPeerServicer
from nutellamd_pb2 import TestMessage, Address, File, SearchMessage, SearchResponse
import grpc
from typing import List


class Peer(PeerToPeerServicer):

    def __init__(self, address: Address):
        self.address = address
        self.neighbours: List[Address] = []
        self.files: List[File] = []

    def TestRpc(self, request, context):
        return TestMessage(
            text="NutellaMD"
        )

    def SearchFile(self, request: SearchMessage, context):
        name = request.fileName
        sender = request.addr
        found = False
        for file in self.files:
            if file.name == name:
                print(f"File found in ({self.address.ip},{self.address.port})")
                found = True

        if not found:
            self.search(name)

    def upload(self, name: str, data: str):
        file = File(
            name=name,
            data=data
        )
        self.files.append(file)

    def print_files(self):
        return self.files

    def search(self, name: str):
        """rpc to all neighbours"""
        for neighbour_addr in self.neighbours:
            with grpc.insecure_channel(f'localhost:{neighbour_addr.port}') as channel:
                stub = nutellamd_pb2_grpc.PeerToPeerStub(channel)
                response = stub.SearchFile(
                    SearchMessage(
                        addr=self.address,
                        fileName=name
                    )
                )
                print("Client received " + response.text)


def serve(peer: Peer):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    nutellamd_pb2_grpc.add_PeerToPeerServicer_to_server(
        peer, server)
    server.add_insecure_port(f'localhost:{peer.address.port}')
    server.start()
    server.wait_for_termination()
