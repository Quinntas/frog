from abc import ABC

from generic.typings import OptionalSelectedFieldsType


class Connection(ABC):
    def __init__(self, uri: str):
        self.uri = uri

    def select(self, selected_fields: OptionalSelectedFieldsType = None):
        from generic.queries.select import SelectQuery
        return SelectQuery(self, selected_fields)
