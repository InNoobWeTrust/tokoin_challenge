from typing import Dict
from pprint import pformat

from . import BaseModel, NameMixin

USER_NAME_KEY = 'users'
TICKET_SUBJECT_KEY = 'tickets'

class Organization(BaseModel, NameMixin):
    def __init__(self, obj: Dict) -> None:
        super().__init__(obj)

    def add_ticket_subject(self, subject):
        if self.data[TICKET_SUBJECT_KEY] is None:
            self.data[TICKET_SUBJECT_KEY] = [subject, ]
        else:
            self.data[TICKET_SUBJECT_KEY].append(subject)

    def add_user_name(self, name: str):
        if self.data[USER_NAME_KEY] is None:
            self.data[USER_NAME_KEY] = [name,]
        else:
            self.data[USER_NAME_KEY].append(name)

