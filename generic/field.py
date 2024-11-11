class Field:
    def __init__(self,
                 name: str,
                 field_type: str,
                 nullable: bool = False
                 ) -> None:
        self.name: str = name
        self.field_type: str = field_type
        self.nullable: bool = nullable
