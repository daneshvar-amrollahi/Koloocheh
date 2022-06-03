from typing import Tuple
from koloocheh_pb2 import Address


class AddressTupleSerializer:
    @staticmethod
    def to_tuple(address: Address):
        return address.ip, address.port

    @staticmethod
    def to_address(tuple_: Tuple[int, int]):
        return Address(ip=tuple_[0], port=tuple_[1])

