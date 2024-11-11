from typing import Optional

from generic.condition import Condition
from generic.conditions.eq import EQ
from generic.connection import Connection
from generic.typings import OptionalSelectedFieldsType, OptionalTableType, OptionalConditionType
from utils.get_fields_from_table import get_fields_from_table


class SelectQuery:
    def __init__(self, connection: Connection, selected_fields: OptionalSelectedFieldsType = None):
        self.connection: Connection = connection
        self.selected_fields: OptionalSelectedFieldsType = selected_fields
        self.table: OptionalTableType = None
        self.where_condition: OptionalConditionType = None
        self.limit: Optional[int] = None
        self.offset: Optional[int] = None

    def from_table(self, table: OptionalTableType):
        self.table = table
        return self

    def where(self, condition: Condition):
        self.where_condition = condition
        return self

    def limit(self, limit: int):
        self.limit = limit
        return self

    def offset(self, offset: int):
        self.offset = offset
        return self

    def execute(self):
        table_name = self.table.Meta.table_name

        if self.selected_fields is None:
            fields = get_fields_from_table(self.table)
            selected_fields = [field[0] for field in fields]
        else:
            selected_fields = list(self.selected_fields.keys())

        query = f"""SELECT {', '.join(selected_fields)} FROM {table_name}"""

        if self.where_condition is not None:
            if isinstance(self.where_condition, EQ):
                query += f" WHERE {self.where_condition.field.name} = ?"

        if self.limit is not None:
            query += f" LIMIT {self.limit}"

        if self.offset is not None:
            query += f" OFFSET {self.offset}"

        return query, self.where_condition.value if self.where_condition is not None else None
