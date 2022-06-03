import sys, logging
from peer_interface import PeerInterface
from nutellamd_pb2 import Address
from master import Master
from const import Const


def main():
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) > 1:
        if sys.argv[1] == "master":
            master = Master(
                Address(
                    ip=Const.MASTER_ADDRESS.ip,
                    port=Const.MASTER_ADDRESS.port
                )
            )
            master.run()

        elif sys.argv[1] == "peer":
            ip, port = list(map(int, sys.argv[2:4]))
            address = Address(
                ip=ip,
                port=port
            )
            peer_interface = PeerInterface(address)
            peer_interface.advertise_to_master(address)
            peer_interface.run()


if __name__ == "__main__":
    main()
