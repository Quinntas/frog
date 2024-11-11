from generic.field import Field


class Varchar(Field):
    def __init__(self,
                 field_name: str,
                 length: int,
                 nullable: bool = False
                 ) -> None:
        super().__init__(
            field_name=field_name,
            field_type=f'VARCHAR({length})',
            nullable=nullable
        )
