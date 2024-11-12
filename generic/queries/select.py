from enum import Enum
from typing import Optional

from generic.condition import Condition
from generic.conditions.eq import EQ
from generic.connection import Connection
from generic.field import Field
from generic.query import Query
from generic.typings import OptionalSelectedFieldsType, OptionalConditionType, TableType
from utils.get_fields_from_table import get_fields_from_table


class JoinType(Enum):
    INNER = 'INNER'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    FULL = 'FULL'


class SelectQuery(Query):
    def __init__(self, connection: Connection, selected_fields: OptionalSelectedFieldsType = None):
        super().__init__(connection)
        self._selected_fields: OptionalSelectedFieldsType = selected_fields
        self._where_condition: OptionalConditionType = None
        self._limit: Optional[int] = None
        self._offset: Optional[int] = None

        self._joins: list[tuple[JoinType, TableType, EQ]] = []

    def from_table(self, table: TableType):
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

    def inner_join(self, table: TableType, on: EQ):
        self._joins.append((JoinType.INNER, table, on))
        return self

    def left_join(self, table: TableType, on: EQ):
        self._joins.append((JoinType.LEFT, table, on))
        return self

    def right_join(self, table: TableType, on: EQ):
        self._joins.append((JoinType.RIGHT, table, on))
        return self

    def full_join(self, table: TableType, on: EQ):
        self._joins.append((JoinType.FULL, table, on))
        return self

    def execute(self):
        table_name = self._table.Meta.table_name

        selected_fields = (
            [field.field_name for field in get_fields_from_table(self._table)]
            if self._selected_fields is None
            else [
                f"{field.field_name_to_sql()} as {field_alias}"
                for field_alias, field in self._selected_fields.items()
            ]
        )

        query = f"SELECT {', '.join(selected_fields)} FROM {table_name}"

        parameters = tuple()

        if self._where_condition is not None and isinstance(self._where_condition, Condition):
            query += f" WHERE {self._where_condition.to_sql()}"
            parameters += self._where_condition.to_value()

        if len(self._joins) > 0:
            for join_type, table, on in self._joins:
                if isinstance(on.value, Field) is not True:
                    raise TypeError("The value of the on condition must be a Field")
                query += f" {join_type.value} JOIN {table.Meta.table_name} ON {on.field.field_name_to_sql()} = {on.value.field_name_to_sql()}"

        if self._limit is not None:
            query += f" LIMIT {self._limit}"

        if self._offset is not None:
            query += f" OFFSET {self._offset}"

        return query, parameters
