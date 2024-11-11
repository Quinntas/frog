from abc import ABC
from typing import Any, List

from generic.condition import Condition
from generic.field import Field


class IN(Condition, ABC):
    def __init__(self, field: Field, values: List[Any]):
        super().__init__(field)
        self.field = field
        self.values = values

    def to_sql(self) -> str:
        return f"{self.field.field_name_to_sql()} IN ({','.join(['?' for _ in self.values])})"


def in_array(field: Field, values: List[Any]):
    return IN(field, values)
