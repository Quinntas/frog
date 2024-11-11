from abc import ABC
from typing import List

from generic.typings import OptionalSelectedFieldsType, TableType
from utils.get_fields_from_table import get_fields_from_table


class Connection(ABC):
    def __init__(self, uri: str, schema: List[TableType]):
        self.uri = uri
        self.schema = schema

    def select(self, selected_fields: OptionalSelectedFieldsType = None):
        from generic.queries.select import SelectQuery
        return SelectQuery(self, selected_fields)

    def insert(self):
        from generic.queries.insert import InsertQuery
        return InsertQuery(self)

    def update(self):
        from generic.queries.update import UpdateQuery
        return UpdateQuery(self)

    def create_tables_from_schema(self):
        queries = [
            f"CREATE TABLE IF NOT EXISTS {table.Meta.table_name}(" +
            ", ".join(field.to_sql() for field in get_fields_from_table(table)) +
            "); "
            for table in self.schema
        ]
        return "".join(queries)
