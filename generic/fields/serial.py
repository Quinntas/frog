from generic.field import Field


class Serial(Field):
    def __init__(self,
                 field_name: str,
                 ) -> None:
        super().__init__(field_name=field_name, field_type='SERIAL')
