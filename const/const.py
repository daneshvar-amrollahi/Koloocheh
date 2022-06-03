from nutellamd_pb2 import Address


class Const:
    MASTER_ADDRESS = Address(
        ip=1,
        port=54321
    )

    class Peer:
        GET_NEIGHBOUR_RATE = 5
        IDENTIFIER_LENGTH = 10