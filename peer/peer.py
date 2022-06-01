from concurrent import futures

import nutellamd_pb2
import nutellamd_pb2_grpc
from nutellamd_pb2_grpc import PeerToPeerServicer
from nutellamd_pb2 import TestMessage
import grpc

class Peer(PeerToPeerServicer):

    def TestRpc(self, request, context):
        return TestMessage(
            text="NutellaMD"
        )

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = nutellamd_pb2_grpc.PeerToPeerStub(channel)
        response = stub.TestRpc(nutellamd_pb2.TestMessage(
            text='Hello NutellaMD!'
        ))
        print("Client received " + response.text)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    nutellamd_pb2_grpc.add_PeerToPeerServicer_to_server(
        Peer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()