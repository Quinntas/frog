from abc import ABC, abstractmethod
from typing import List, Any

from generic.typings import TableType, SelectedFieldsType
from utils.get_fields_from_table import get_fields_from_table


class Connection(ABC):
    def __init__(self, uri: str, schema: List[TableType]):
        self.uri = uri
        self.schema = schema

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def execute(self, query: str, parameters: tuple[Any]):
        pass

    @abstractmethod
    async def close(self):
        pass

    @abstractmethod
    async def query(self, query: str, *args):
        pass

    def select(self, selected_fields: SelectedFieldsType):
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
