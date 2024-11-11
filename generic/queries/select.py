from typing import Optional

from generic.condition import Condition
from generic.conditions.eq import EQ
from generic.connection import Connection
from generic.typings import OptionalSelectedFieldsType, OptionalTableType, OptionalConditionType
from utils.get_fields_from_table import get_fields_from_table


class SelectQuery:
    def __init__(self, connection: Connection, selected_fields: OptionalSelectedFieldsType = None):
        self._connection: Connection = connection
        self._selected_fields: OptionalSelectedFieldsType = selected_fields
        self._table: OptionalTableType = None
        self._where_condition: OptionalConditionType = None
        self._limit: Optional[int] = None
        self._offset: Optional[int] = None

    def from_table(self, table: OptionalTableType):
        self._table = table
        return self

    def where(self, condition: Condition):
        self._where_condition = condition
        return self

    def limit(self, limit: int):
        self._limit = limit
        return self

    def offset(self, offset: int):
        self._offset = offset
        return self

    def execute(self):
        table_name = self._table.Meta.table_name

        if self._selected_fields is None:
            selected_fields = [field.name for field in get_fields_from_table(self._table)]
        else:
            selected_fields = [
                f"{field.table.Meta.table_name}.{field.name} as {field_alias}"
                for field_alias, field in self._selected_fields.items()
            ]

        query = f"""SELECT {', '.join(selected_fields)} FROM {table_name}"""

        if self._where_condition is not None:
            if isinstance(self._where_condition, EQ):
                query += f" WHERE {self._where_condition.field.name} = ?"

        if self._limit is not None:
            query += f" LIMIT {self._limit}"

        if self._offset is not None:
            query += f" OFFSET {self._offset}"

        return query, self._where_condition.value if self._where_condition is not None else None
