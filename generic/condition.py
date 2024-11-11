from abc import ABC, abstractmethod
from typing import Optional

from generic.field import Field


class Condition(ABC):
    def __init__(self, field: Optional[Field] = None):
        self.field = field

    @abstractmethod
    def to_sql(self) -> str:
        pass
