from typing import Dict

from tokoin_challenge.model.base_model import BaseModel


SUBMITTER_ID_KEY = 'submitter_id'
ASSIGNEE_ID_KEY = 'assignee_id'
ORG_ID_KEY = 'organization_id'
SUBMITTER_NAME_KEY = 'submitter_name'
ASSIGNEE_NAME_KEY = 'assignee_name'
ORG_NAME_KEY = 'organization_name'
SUBJECT_KEY = 'subject'

class Ticket(BaseModel):
    def __init__(self, obj: Dict):
        super().__init__(obj)

    @property
    def submitter_ref(self) -> int or None:
        return self.data.get(SUBMITTER_ID_KEY)

    @property
    def assignee_ref(self) -> int or None:
        return self.data.get(ASSIGNEE_ID_KEY)

    @property
    def org_ref(self) -> int or None:
        return self.data.get(ORG_ID_KEY)

    @property
    def subject(self) -> str:
        return self.data[SUBJECT_KEY]

    @property
    def is_submitter_set(self) -> bool:
        return self.submitter_ref is None or self.data.get(SUBMITTER_NAME_KEY) is not None

    def set_submitter_name(self, name: str):
        self._data[SUBMITTER_NAME_KEY] = name

    @property
    def is_assignee_set(self) -> bool:
        return self.assignee_ref is None or self.data.get(ASSIGNEE_NAME_KEY) is not None

    def set_assignee_name(self, name: str):
        self._data[ASSIGNEE_NAME_KEY] = name

    def set_org_name(self, name: str):
        self._data[ORG_NAME_KEY] = name
