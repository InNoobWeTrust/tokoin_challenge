NAME_KEY = "name"


class NameMixin:

    @property
    def name(self) -> str:
        return self.__dict__["_data"][NAME_KEY]
