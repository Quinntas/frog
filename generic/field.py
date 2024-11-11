# generic/field.py
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from generic.table import Table


class Field:
    def __init__(self,
                 name: str,
                 field_type: str,
                 nullable: bool = False,
                 table: Optional['Table'] = None
                 ) -> None:
        self.name: str = name
        self.field_type: str = field_type
        self.nullable: bool = nullable
        self.table: Optional['Table'] = table
