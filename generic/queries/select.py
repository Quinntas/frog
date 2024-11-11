from typing import Optional

from generic.condition import Condition
from generic.connection import Connection
from generic.query import Query
from generic.typings import OptionalSelectedFieldsType, OptionalConditionType, TableType
from utils.get_fields_from_table import get_fields_from_table


class SelectQuery(Query):
    def __init__(self, connection: Connection, selected_fields: OptionalSelectedFieldsType = None):
        super().__init__(connection)
        self._selected_fields: OptionalSelectedFieldsType = selected_fields
        self._where_condition: OptionalConditionType = None
        self._limit: Optional[int] = None
        self._offset: Optional[int] = None

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

    @property
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

        parameters = []
        if self._where_condition is not None and isinstance(self._where_condition, Condition):
            query += f" WHERE {self._where_condition.to_sql()}"

        if self._limit is not None:
            query += f" LIMIT {self._limit}"

        if self._offset is not None:
            query += f" OFFSET {self._offset}"

        return query, tuple(parameters)
