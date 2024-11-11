from generic.field import Field


class ForeignKey(Field):
    def __init__(self,
                 field_name: str,
                 field: Field,
                 nullable: bool = False,
                 ) -> None:
        super().__init__(
            field_name=field_name,
            field_type=field.field_type,
            reference=field,
            nullable=nullable
        )
