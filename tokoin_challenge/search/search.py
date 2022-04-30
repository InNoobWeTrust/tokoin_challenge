from tokoin_challenge import config
from tokoin_challenge.config.config import read_config


def search_user():
    conf = read_config()
    user_data_path = conf['User']
    ticket_data_path = conf['Ticket']
    org_data_path = conf['Organization']
