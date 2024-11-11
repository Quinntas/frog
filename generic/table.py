from typing import Type


class Table:
    class Meta:
        table_name: str

    Meta: Type[Meta]
