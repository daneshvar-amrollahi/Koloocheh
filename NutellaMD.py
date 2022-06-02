import sys
from peer_interface import PeerInterface
from nutellamd_pb2 import Address


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "master":
            pass
        elif sys.argv[1] == "peer":
            ip = int(sys.argv[2])
            port = int(sys.argv[3])
            peer_interface = PeerInterface(
                Address(
                    ip=ip,
                    port=port
                )
            )
            peer_interface.run()


if __name__ == "__main__":
    main()
