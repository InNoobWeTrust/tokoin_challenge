from .config import read_config

def test_read_config():
    conf = read_config()
    print(conf)
    assert conf == {
        'Organization': 'data/organizations.json',
        'User': 'data/users.json',
        'Ticket': 'data/tickets.json',
    }
