from typing import Dict

from . import BaseModel, NameMixin

ORG_ID_KEY = 'organization_id'
ORG_NAME_KEY = 'organization_name'
ASSIGNED_TICKET_KEY = 'assigned_ticket'
SUBMITTED_TICKET_KEY = 'submitted_subject'

class User(BaseModel, NameMixin):
    def __init__(self, obj: Dict) -> None:
        super().__init__(obj)

    @property
    def org_ref(self) -> int:
        return self.data[ORG_ID_KEY]

    def set_org_name(self, name: str):
        self.data[ORG_NAME_KEY] = name

    def add_assigned_ticket(self, subject: str):
        if self.data[ASSIGNED_TICKET_KEY] is None:
            self.data[ASSIGNED_TICKET_KEY] = [subject,]
        else:
            self.data[ASSIGNED_TICKET_KEY].append(subject)

    def add_submitted_ticket(self, subject: str):
        if self.data[SUBMITTED_TICKET_KEY] is None:
            self.data[SUBMITTED_TICKET_KEY] = [subject,]
        else:
            self.data[SUBMITTED_TICKET_KEY].append(subject)