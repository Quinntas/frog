from generic.field import Field


class ForeignKey(Field):
    def __init__(self,
                 field_name: str,
                 field: Field,
                 nullable: bool = False,
                 ) -> None:
        super().__init__(name=field_name, field_type=field.field_type, nullable=nullable)
        self.field: Field = field
