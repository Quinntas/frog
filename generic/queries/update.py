from typing import Any

from generic.condition import Condition
from generic.connection import Connection
from generic.field import Field
from generic.query import Query
from generic.typings import OptionalConditionType, TableType


class UpdateQuery(Query):
    def __init__(self, connection: Connection):
        super().__init__(connection)
        self._set_values = {}
        self._where_condition: OptionalConditionType = None

    def table(self, table: TableType):
        self._table = table
        return self

    def set(self, field: Field, value: Any):
        self._set_values[field] = value
        return self

    def where(self, condition: Condition):
        self._where_condition = condition
        return self

    def execute(self):
        set_clause = ', '.join([f"{field.field_name} = ?" for field in self._set_values.keys()])
        query = f"UPDATE {self._table.Meta.table_name} SET {set_clause}"

        parameters = list(self._set_values.values())
        if self._where_condition is not None and isinstance(self._where_condition, Condition):
            query += f" WHERE {self._where_condition.to_sql()}"
            parameters.append(self._where_condition.value)

        return query, tuple(parameters)
