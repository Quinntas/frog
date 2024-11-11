from abc import ABC, abstractmethod

from generic.field import Field


class Condition(ABC):
    def __init__(self, field: Field):
        self.field = field

    @abstractmethod
    def to_sql(self) -> str:
        pass
