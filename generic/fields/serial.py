from generic.field import Field


class Serial(Field):
    def __init__(self,
                 field_name: str,
                 primary_key: bool = False,
                 nullable: bool = False
                 ) -> None:
        super().__init__(field_name=field_name, field_type='SERIAL', nullable=nullable, primary_key=primary_key)
