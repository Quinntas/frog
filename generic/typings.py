from typing import Type, Optional

from generic.condition import Condition
from generic.field import Field
from generic.table import Table

TableType = Type[Table]

OptionalTableType = Optional[TableType]

SelectedFieldsType = dict[str, Field]

OptionalSelectedFieldsType = Optional[SelectedFieldsType]

OptionalConditionType = Optional[Condition]
