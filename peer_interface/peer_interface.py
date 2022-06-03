import logging

from peer import Peer, serve
from nutellamd_pb2 import Address
from threading import Thread


class PeerInterface:

    def __init__(self, address: Address):
        self.peer = Peer(address)

    def run(self):
        t = Thread(
            target=serve,
            args=(self.peer,)
        )
        t.start()

        try:
            while True:
                self.handle_command()
        except KeyboardInterrupt:
            exit(1)

    def handle_command(self):
        command = list(map(str, input().split()))
        if command[0] == "search":
            name = command[1]
            self.peer.search(
                name=name
            )
        if command[0] == "upload":
            name, data = command[1:]
            self.peer.upload(
                name=name,
                data=data
            )

        if command[0] == "get_files":
            print(self.peer.print_files())

        if command[0] == "add_neighbour":
            ip, port = list(map(int, command[1:]))
            self.peer.add_neighbour(
                Address(
                    ip=ip,
                    port=port
                )
            )