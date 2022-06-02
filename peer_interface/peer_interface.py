from peer import Peer
from nutellamd_pb2 import Address


class PeerInterface:

    def __init__(self, address: Address):
        self.peer = Peer(address)

    def run(self):
        while True:
            command = list(map(str, input().split()))
            if command[0] == "search":
                pass
            if command[0] == "upload":
                name = command[1]
                data = command[2]
                self.peer.upload(
                    name=name,
                    data=data
                )
            if command[0] == "get_files":
                print(self.peer.print_files())
