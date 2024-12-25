from generic.field import Field


class ForeignKey(Field):
    def __init__(self,
                 field_name: str,
                 field: Field,
                 ) -> None:
        super().__init__(
            field_name=field_name,
            field_type=field.field_type,
            reference=field,
            python_type=field.python_type,
        )
