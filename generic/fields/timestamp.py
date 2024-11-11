from generic.field import Field


class Timestamp(Field):
    def __init__(self, field_name: str, auto_now_add: bool = False, field_nullable: bool = False):
        super().__init__(name=field_name, field_type='timestamp', nullable=field_nullable)
        self.auto_now_add = auto_now_add
