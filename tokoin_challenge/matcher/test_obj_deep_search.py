from tokoin_challenge.matcher.obj_deep_search import is_deep_contain


dummy_obj = {
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

def test_deep_contain():
    for term in [
            1,
            'http://initech.tokoin.io.com/api/v2/users/1.json',
            '74341f74-9c79-49d5-9611-87ef9b6eb75f',
            'Miss Coffey',
            '2016-04-15T05:19:46 -10:00',
            'coffeyrasmussen@flotonic.com',
            '8335-422-718',
            "Don't Worry Be Happy!",
            'Springville',
            True,
    ]:
        assert is_deep_contain(dummy_obj, term)
