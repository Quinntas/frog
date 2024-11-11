from generic.condition import Condition
from generic.conditions.eq import EQ
from generic.connection import Connection
from generic.query import Query
from generic.typings import OptionalTableType, OptionalConditionType


class UpdateQuery(Query):
    def __init__(self, connection: Connection):
        super().__init__(connection)
        self._set_values = {}
        self._where_condition: OptionalConditionType = None

    def table(self, table: OptionalTableType):
        self._table = table
        return self

    def set(self, field, value):
        self._set_values[field] = value
        return self

    def where(self, condition: Condition):
        self._where_condition = condition
        return self

    def execute(self):
        table_name = self._table.Meta.table_name
        set_clause = ', '.join([f"{field.name} = ?" for field in self._set_values.keys()])
        query = f"UPDATE {table_name} SET {set_clause}"

        if self._where_condition is not None:
            if isinstance(self._where_condition, EQ):
                query += f" WHERE {self._where_condition.field.name} = ?"

        parameters = list(self._set_values.values())
        if self._where_condition is not None:
            parameters.append(self._where_condition.value)

        return query, tuple(parameters)
