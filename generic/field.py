# generic/field.py
from collections.abc import Callable
from typing import Optional, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generic.table import Table


class Field:
    def __init__(self,
                 field_name: str,
                 field_type: str,
                 nullable: bool = False,
                 primary_key: bool = False,
                 reference: Optional['Field'] = None,
                 table: Optional['Table'] = None
                 ) -> None:
        self.field_name: str = field_name
        self.field_type: str = field_type
        self.nullable: bool = nullable
        self.table: Optional['Table'] = table
        self.default_value_fn: Optional[Callable[[], Any]] = None
        self._primary_key: bool = primary_key
        self.reference: Optional['Field'] = reference

    def not_null(self):
        self.nullable = False
        return self

    def primary_key(self):
        self._primary_key = True
        return self

    def to_sql(self) -> str:
        field_sql = f"{self.field_name} {self.field_type}"
        if not self.nullable:
            field_sql += " NOT NULL"
        if self._primary_key:
            field_sql += " PRIMARY KEY"
        if self.reference:
            field_sql += f" REFERENCES {self.reference.field_name_to_sql()})"
        return field_sql

    def field_name_to_sql(self) -> str:
        return f"{self.table.Meta.table_name}.{self.field_name}"

    def default(self, default_value_fn: Callable[[], Any]) -> 'Field':
        self.default_value_fn = default_value_fn
        return self
