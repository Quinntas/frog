from abc import ABC

from generic.condition import Condition


class OrCondition(Condition, ABC):
    def __init__(self, *conditions: Condition):
        super().__init__()
        self._conditions = conditions

    def to_sql(self) -> str:
        return f"({' OR '.join([condition.to_sql() for condition in self._conditions])})"


def or_condition(*conditions: Condition) -> OrCondition:
    return OrCondition(*conditions)
