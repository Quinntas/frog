from generic.field import Field
from generic.typings import TableType


class ForeignKey:
    def __init__(self,
                 table: TableType,
                 field: Field
                 ):
        self.table: TableType = table
        self.field: Field = field
