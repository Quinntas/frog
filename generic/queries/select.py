from generic.condition import Condition
from generic.conditions.eq import EQ
from generic.connection import Connection
from generic.typings import OptionalSelectedFieldsType, OptionalTableType, OptionalConditionType


class SelectQuery:
    def __init__(self, connection: Connection, selected_fields: OptionalSelectedFieldsType = None):
        self.connection: Connection = connection
        self.selected_fields: OptionalSelectedFieldsType = selected_fields
        self.table: OptionalTableType = None
        self.where_condition: OptionalConditionType = None

    def from_table(self, table: OptionalTableType):
        self.table = table
        return self

    def where(self, condition: Condition):
        self.where_condition = condition
        return self

    def execute(self):
        table_name = self.table.Meta.table_name

        where = ""

        if self.where_condition is not None:
            if isinstance(self.where_condition, EQ):
                where = f"WHERE {self.where_condition.field.name} = ?"

        return f"""SELECT * FROM {table_name} {where}""", self.where_condition.value
