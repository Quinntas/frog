from abc import ABC, abstractmethod
from typing import Optional, Any

from generic.field import Field


class Condition(ABC):
    def __init__(self, field: Optional[Field] = None):
        self.field = field

    @abstractmethod
    def to_sql(self) -> str:
        pass

    @abstractmethod
    def to_value(self) -> tuple[Any]:
        pass
