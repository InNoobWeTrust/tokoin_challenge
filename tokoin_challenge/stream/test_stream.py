from io import BytesIO, TextIOWrapper
import json
from unittest.mock import mock_open, patch

from tokoin_challenge.stream.data_stream import obj_streamer


dummy_data = '''
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
      "Hartsville/Hartley",
      "Diaperville"
    ],
    "suspended": true,
    "role": "admin"
  }
]
'''

m = mock_open()
m.side_effect = lambda _file_name, _mode: TextIOWrapper(BytesIO(bytes(dummy_data, 'utf-8')))

@patch('builtins.open', m)
def test_obj_streamer():
    obj = next(obj_streamer(''))
    print(json.dumps(obj))
    assert obj == {
    "_id": 1,
    "url": "http://initech.tokoin.io.com/api/v2/users/1.json",
    "external_id": "74341f74-9c79-49d5-9611-87ef9b6eb75f",
    "name": "Francisca Rasmussen",
    "alias": "Miss Coffey",
    "created_at": "2016-04-15T05:19:46 -10:00",
    "active": True,
    "verified": True,
    "shared": False,
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
      "Hartsville/Hartley",
      "Diaperville"
    ],
    "suspended": True,
    "role": "admin"
    }

test_obj_streamer()
