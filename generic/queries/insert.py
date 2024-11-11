from generic.connection import Connection
from generic.field import Field
from generic.query import Query
from generic.typings import OptionalConditionType


class InsertQuery(Query):
    def __init__(self, connection: Connection):
        super().__init__(connection)
        self._where_condition: OptionalConditionType = None
        self._values = {}

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
        self._values.update({
            field.name: field.default_value_fn()
            for field in self._table.__dict__.values()
            if isinstance(field, Field) and field.default_value_fn and field.name not in self._values
        })

        keys = ', '.join(self._values.keys())
        parameters = ', '.join(['?' for _ in self._values])

        query = f"INSERT INTO {self._table.Meta.table_name} ({keys}) VALUES ({parameters})"
        return query, tuple(self._values.values())
