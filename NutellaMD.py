import sys, logging
from peer_interface import PeerInterface
from nutellamd_pb2 import Address


def main():
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) > 1:
        if sys.argv[1] == "master":
            pass
        elif sys.argv[1] == "peer":
            ip, port = list(map(int, sys.argv[2:4]))
            peer_interface = PeerInterface(
                Address(
                    ip=ip,
                    port=port
                )
            )

            peer_interface.run()


if __name__ == "__main__":
    main()
