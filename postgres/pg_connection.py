from abc import ABC

from generic.connection import Connection


class Postgres(Connection, ABC):
    def __init__(self, uri: str):
        super().__init__(uri)
