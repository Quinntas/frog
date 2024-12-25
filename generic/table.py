from typing import Type

from generic.field import Field


class TableMeta(type):
    def __new__(cls, name, bases, dct):
        table_class = super().__new__(cls, name, bases, dct)

        for attr_name, attr_value in dct.items():
            if isinstance(attr_value, Field):
                attr_value.table = table_class
                setattr(table_class, attr_name, attr_value)

        return table_class


class Table(metaclass=TableMeta):
    class Meta:
        table_name: str

    Meta: Type[Meta]
