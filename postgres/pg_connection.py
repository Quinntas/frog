from abc import ABC
from typing import List, Optional

from generic.connection import Connection
from generic.typings import TableType


class Postgres(Connection, ABC):
    def __init__(self, uri: str, schema: Optional[List[TableType]] = None):
        super().__init__(uri, schema or [])
