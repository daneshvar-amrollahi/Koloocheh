from koloocheh_pb2 import Address


class Const:
    MASTER_ADDRESS = Address(
        ip='localhost',
        port=54321
    )

    class Peer:
        GET_NEIGHBOUR_RATE = 5
        IDENTIFIER_LENGTH = 10
        CHECK_LIVENESS_RATE = GET_NEIGHBOUR_RATE * 4
        QUERY_TTL = 10
