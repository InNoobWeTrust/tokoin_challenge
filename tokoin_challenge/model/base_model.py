from pprint import pformat
from typing import Dict

ID_KEY = "_id"


class BaseModel:

    def __init__(self, obj: Dict) -> None:
        self._data = obj

    @property
    def id(self) -> str:
        return self.data[ID_KEY]

    @property
    def data(self) -> Dict:
        if not self._data:
            raise Exception("Not initialized with correct data")

        return self._data

    def __repr__(self) -> str:
        return pformat(self._data, indent=4, compact=False, sort_dicts=True)
