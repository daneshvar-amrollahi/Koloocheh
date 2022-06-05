import koloocheh_pb2_grpc
from peer import Peer, serve
from const import const
from koloocheh_pb2 import Address
from threading import Thread, Timer
import grpc
import logging


class PeerInterface:

    def __init__(self, address: Address):
        self.peer = Peer(address)
        self.logger = logging.getLogger(__name__)

    def run(self):
        thread_run = Thread(
            target=serve,
            args=(self.peer,),
            daemon=True
        )
        thread_run.start()

        thread_get_neighbours = Thread(
            target=self.peer.get_neighbours,
            daemon=True
        )
        thread_get_neighbours.start()

        thread_query_results = Thread(
            target=self.peer.check_query_results,
            daemon=True
        )
        thread_query_results.start()

        try:
            while True:
                self.handle_command()
        except KeyboardInterrupt:
            exit(0)

    def handle_command(self):
        command = list(map(str, input().split()))
        if command[0] == "download":
            name = command[1]
            self.peer.download(name=name)
        if command[0] == "upload":
            name, data = command[1:]
            self.peer.upload(
                name=name,
                data=data
            )
            self.logger.info(f"Peer with ip={self.peer.address.ip}, port={self.peer.address.port} uploaded file {name} with data: {data}")

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

    def advertise_to_master(self):
        self.peer.advertise_to_master()

