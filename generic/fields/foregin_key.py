from generic.field import Field
from generic.table import Table


class ForeignKey(Field):
    def __init__(self,
                 field_name: str,
                 table: Table,
                 field: Field,
                 nullable: bool = False,
                 ) -> None:
        super().__init__(name=field_name, field_type=field.field_type, nullable=nullable)
        self.field: Field = field
        self.table: Table = table
