from typing import Any

from generic.condition import Condition
from generic.connection import Connection
from generic.field import Field
from generic.query import Query
from generic.typings import OptionalConditionType, TableType
from utils.get_fields_from_table import get_fields_from_table


class InsertQuery(Query):
    def __init__(self, connection: Connection):
        super().__init__(connection)
        self._where_condition: OptionalConditionType = None
        self._values = {}

    def into(self, table: TableType):
        self._table = table
        return self

    def values(self, values: dict[str, Any]):
        self._values = values
        return self

    def where(self, condition: Condition):
        self._where_condition = condition
        return self

    def execute(self):
        self._values.update({
            field.field_name: field.default_value_fn()
            for field in get_fields_from_table(self._table)
            if isinstance(field, Field) and field.default_value_fn and field.field_name not in self._values
        })

        keys = ', '.join(self._values.keys())
        parameters = ', '.join(['?' for _ in self._values])

        query = f"INSERT INTO {self._table.Meta.table_name} ({keys}) VALUES ({parameters})"
        return query, tuple(self._values.values())
