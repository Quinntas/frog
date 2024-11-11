from typing import Type

from generic.field import Field


class Table:
    class Meta:
        table_name: str

    Meta: Type[Meta]

    def get_fields(self):
        fields = []
        for field_name in dir(self):
            field = getattr(self, field_name)
            if isinstance(field, Field):
                fields.append(field)
        return fields
