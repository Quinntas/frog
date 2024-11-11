from abc import ABC
from typing import Any

from generic.condition import Condition
from generic.field import Field


class LTE(Condition, ABC):
    def __init__(self, field: Field, value: Any):
        super().__init__(field)
        self.field = field
        self.value = value

    def to_sql(self) -> str:
        return f"{self.field.field_name_to_sql()} <= ?"


def lte(field: Field, value: Any):
    return LTE(field, value)
