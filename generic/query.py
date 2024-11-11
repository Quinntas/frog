from generic.connection import Connection
from generic.typings import OptionalTableType


class Query:
    def __init__(self, connection: Connection):
        self._connection: Connection = connection
        self._table: OptionalTableType = None
