from datetime import datetime

from generic.field import Field


class Timestamp(Field):
    def __init__(self,
                 field_name: str,
                 auto_now_add: bool = False,
                 ) -> None:
        super().__init__(
            field_name=field_name,
            field_type=f'TIMESTAMP {"DEFAULT CURRENT_TIMESTAMP" if auto_now_add else ""}',
            python_type=datetime,
        )
