from generic.connection import Connection
from generic.query import Query
from generic.typings import OptionalConditionType


class InsertQuery(Query):
    def __init__(self, connection: Connection):
        super().__init__(connection)
        self._where_condition: OptionalConditionType = None
        self._values = None

    def into(self, table):
        self._table = table
        return self

    def values(self, values):
        self._values = values
        return self

    def where(self, condition):
        self._where_condition = condition
        return self

    def execute(self):
        table_name = self._table.Meta.table_name
        keys = ', '.join(self._values.keys())
        parameters = ', '.join(['?' for _ in self._values])
        query = f"INSERT INTO {table_name} ({keys}) VALUES ({parameters})"
        return query, tuple(self._values.values())
