from generic.field import Field


class Serial(Field):
    primary_key: bool = False

    def __init__(self,
                 field_name: str,
                 primary_key: bool = False,
                 field_nullable: bool = False
                 ):
        super().__init__(name=field_name, field_type='serial', nullable=field_nullable)
        self.primary_key: bool = primary_key
