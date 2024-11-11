from typing import Type, List

from generic.field import Field


def get_fields_from_table(cls: Type) -> List[Field]:
    return [
        value
        for name, value in cls.__dict__.items()
        if isinstance(value, Field)
    ]
