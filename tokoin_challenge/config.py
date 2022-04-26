from os import path, curdir

config_path = path.join(curdir, 'config', 'default.toml')

def read_config():
    data = {}
    with open(config_path, 'r') as conf:
        conf.read_line()
        org, org_path = conf.read_line().split(' = ')
        usr, usr_path = conf.read_line().split(' = ')
        ticket, ticket_path = conf.read_line().split(' = ')

        for attr in ['org', 'usr', 'ticket']:
            data[locals()[attr]] = locals()[attr + '_path']

    return data
