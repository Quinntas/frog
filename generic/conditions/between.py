from abc import ABC
from typing import Any

from generic.condition import Condition
from generic.field import Field


class BETWEEN(Condition, ABC):
    def __init__(self, field: Field, lower_value: Any, upper_value: Any):
        super().__init__(field)
        self.lower_value = lower_value
        self.upper_value = upper_value

    def to_sql(self) -> str:
        return f"{self.field.field_name_to_sql()} BETWEEN ? AND ?"

    def to_value(self) -> tuple[Any, Any]:
        return self.lower_value, self.upper_value


def between(field: Field, lower_value: Any, upper_value: Any):
    return BETWEEN(field, lower_value, upper_value)
