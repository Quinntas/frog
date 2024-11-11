from generic.field import Field


class Serial(Field):
    primary_key: bool = False

    def __init__(self,
                 field_name: str,
                 primary_key: bool = False,
                 nullable: bool = False
                 ) -> None:
        super().__init__(name=field_name, field_type='serial', nullable=nullable)
        self.primary_key: bool = primary_key
