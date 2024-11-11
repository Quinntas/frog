from generic.field import Field


class Varchar(Field):
    def __init__(self, field_name: str, length: int, nullable: bool = False):
        super().__init__(name=field_name, field_type=f'varchar({length})', nullable=nullable)
