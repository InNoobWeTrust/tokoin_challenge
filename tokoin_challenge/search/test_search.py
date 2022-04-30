from io import BytesIO, TextIOWrapper
from unittest.mock import mock_open, patch
from tokoin_challenge.matcher.obj_deep_search import is_deep_contain

from tokoin_challenge.search.search import fill_org_meta_data, fill_ticket_metadata, fill_user_metadata, search_org_stream, search_ticket_stream, search_user_stream

dummy_usr_data = '''
[
  {
    "_id": 1,
    "url": "http://initech.tokoin.io.com/api/v2/users/1.json",
    "external_id": "74341f74-9c79-49d5-9611-87ef9b6eb75f",
    "name": "Francisca Rasmussen",
    "alias": "Miss Coffey",
    "created_at": "2016-04-15T05:19:46 -10:00",
    "active": true,
    "verified": true,
    "shared": false,
    "locale": "en-AU",
    "timezone": "Sri Lanka",
    "last_login_at": "2013-08-04T01:03:27 -10:00",
    "email": "coffeyrasmussen@flotonic.com",
    "phone": "8335-422-718",
    "signature": "Don't Worry Be Happy!",
    "organization_id": 119,
    "tags": [
      "Springville",
      "Sutton",
      "Oley",
      "Hartsville/Hartley",
      "Diaperville"
    ],
    "suspended": true,
    "role": "admin"
  },
  {
    "_id": 48,
    "url": "http://initech.tokoin.io.com/api/v2/users/48.json",
    "external_id": "80e6a7b7-9a2a-4b93-93da-68bd5e95cbb8",
    "name": "Pitts Park",
    "alias": "Miss Betsy",
    "created_at": "2016-02-02T03:34:44 -11:00",
    "active": false,
    "verified": true,
    "shared": false,
    "locale": "en-AU",
    "timezone": "Lesotho",
    "last_login_at": "2012-06-01T08:51:56 -10:00",
    "email": "betsypark@flotonic.com",
    "phone": "9974-742-963",
    "signature": "Don't Worry Be Happy!",
    "organization_id": 119,
    "tags": [
      "Chicopee",
      "Maplewood",
      "Oley",
      "Whitmer"
    ],
    "suspended": false,
    "role": "agent"
  }
]
'''

dummy_ticket_data = '''
[
  {
    "_id": "cb304286-7064-4509-813e-edc36d57623d",
    "url": "http://initech.tokoin.io.com/api/v2/tickets/cb304286-7064-4509-813e-edc36d57623d.json",
    "external_id": "df00b850-ca27-4d9a-a91a-d5b8d130a79f",
    "created_at": "2016-03-30T11:43:24 -11:00",
    "type": "task",
    "subject": "A Nuisance in Saint Lucia",
    "description": "Nostrud veniam eiusmod reprehenderit adipisicing proident aliquip. Deserunt irure deserunt ea nulla cillum ad.",
    "priority": "urgent",
    "status": "pending",
    "submitter_id": 1,
    "assignee_id": 48,
    "organization_id": 119,
    "tags": [
      "Missouri",
      "Alabama",
      "Virginia",
      "Virgin Islands"
    ],
    "has_incidents": false,
    "due_at": "2016-08-03T04:44:08 -10:00",
    "via": "chat"
  },
  {
    "_id": "fc5a8a70-3814-4b17-a6e9-583936fca909",
    "url": "http://initech.tokoin.io.com/api/v2/tickets/fc5a8a70-3814-4b17-a6e9-583936fca909.json",
    "external_id": "e8cab26b-f3b9-4016-875c-b0d9a258761b",
    "created_at": "2016-07-08T07:57:15 -10:00",
    "type": "problem",
    "subject": "A Nuisance in Kiribati",
    "description": "Ipsum reprehenderit non ea officia labore aute. Qui sit aliquip ipsum nostrud anim qui pariatur ut anim aliqua non aliqua.",
    "priority": "high",
    "status": "open",
    "submitter_id": 48,
    "assignee_id": 1,
    "organization_id": 119,
    "tags": [
      "Minnesota",
      "New Jersey",
      "Texas",
      "Nevada"
    ],
    "has_incidents": true,
    "via": "voice"
  }
]
'''

dummy_org_data = '''
[
  {
    "_id": 119,
    "url": "http://initech.tokoin.io.com/api/v2/organizations/119.json",
    "external_id": "2386db7c-5056-49c9-8dc4-46775e464cb7",
    "name": "Multron",
    "domain_names": [
      "bleeko.com",
      "pulze.com",
      "xoggle.com",
      "sultraxin.com"
    ],
    "created_at": "2016-02-29T03:45:12 -11:00",
    "details": "Non profit",
    "shared_tickets": false,
    "tags": [
      "Erickson",
      "Mccoy",
      "Wiggins",
      "Brooks"
    ]
  }
]
'''

m = mock_open()


def side_effect(file_name: str, mode: str) -> TextIOWrapper:
    data = None
    if file_name == "data/organizations.json":
        data = dummy_org_data
    elif file_name == "data/users.json":
        data = dummy_usr_data
    elif file_name == "data/tickets.json":
        data = dummy_ticket_data

    return TextIOWrapper(BytesIO(bytes(data, 'utf-8')))


m.side_effect = side_effect


@patch('builtins.open', m)
def test_search_usr():
    records = list(search_user_stream(lambda usr: usr.id == 48))
    assert len(records) == 1
    record = fill_user_metadata(records[0])
    assert record.data.get('organization_name') == "Multron"
    assert isinstance(record.data.get('submitted_tickets'), list)
    assert isinstance(record.data.get('assigned_tickets'), list)

    records = list(
        search_user_stream(lambda usr: is_deep_contain(usr.data, 'Oley')))
    assert len(records) == 2


@patch('builtins.open', m)
def test_search_ticket():
    records = list(
        search_ticket_stream(
            lambda ticket: is_deep_contain(ticket.data, 'urgent')))
    assert len(records) == 1
    record = fill_ticket_metadata(records[0])
    assert record.data.get('submitter_name') == 'Francisca Rasmussen'
    assert record.data.get('assignee_name') == 'Pitts Park'
    assert record.data.get('organization_name') == 'Multron'


@patch('builtins.open', m)
def test_search_org():
    record = list(
        search_org_stream(lambda org: is_deep_contain(org.data, 'Multron')))
    assert len(record) == 1
    record = fill_org_meta_data(record[0])
    assert len(record.data.get('users')) == 2
    assert len(record.data.get('tickets')) == 2
