from abc import ABC

from generic.condition import Condition


class AndCondition(Condition, ABC):
    def __init__(self, *conditions: Condition):
        super().__init__()
        self._conditions = conditions

    def to_sql(self) -> str:
        return f"({' AND '.join([condition.to_sql() for condition in self._conditions])})"


def and_condition(*conditions: Condition) -> AndCondition:
    return AndCondition(*conditions)
