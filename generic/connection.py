from abc import ABC
from typing import List

from generic.fields.foregin_key import ForeignKey
from generic.fields.serial import Serial
from generic.typings import OptionalSelectedFieldsType, TableType
from utils.get_fields_from_table import get_fields_from_table


class Connection(ABC):
    def __init__(self, uri: str, schema: List[TableType]):
        self.uri = uri
        self.schema = schema

    def select(self, selected_fields: OptionalSelectedFieldsType = None):
        from generic.queries.select import SelectQuery
        return SelectQuery(self, selected_fields)

    def create_tables_from_schema(self):
        query = ""
        for table in self.schema:
            query += f"CREATE TABLE IF NOT EXISTS {table.Meta.table_name}(\n"
            fields = get_fields_from_table(table)

            for field in fields:
                field_query = f"\t{field.name} {field.field_type}"

                if isinstance(field, Serial):
                    if field.primary_key is True:
                        field_query += " PRIMARY KEY"
                elif isinstance(field, ForeignKey):
                    field_query += f" REFERENCES {field.field.table.Meta.table_name}({field.field.name})"

                if not field.nullable:
                    field_query += " NOT NULL"

                query += field_query + ", \n"

            query = query[:-3]
            query += "\n);\n"

        return query
