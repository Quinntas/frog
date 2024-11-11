# generic/field.py
from collections.abc import Callable
from typing import Optional, TYPE_CHECKING, Any

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
        self.default_value_fn: Optional[Callable[[], Any]] = None

    def default(self, default_value_fn: Callable[[], Any]) -> 'Field':
        self.default_value_fn = default_value_fn
        return self
