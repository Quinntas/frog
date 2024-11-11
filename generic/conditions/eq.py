from typing import Any

from generic.condition import Condition
from generic.field import Field


class EQ(Condition):
    def __init__(self, field: Field, value: Any):
        self.field = field
        self.value = value


def eq(field: Field, value: Any):
    return EQ(field, value)
