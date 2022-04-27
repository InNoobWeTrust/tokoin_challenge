from os import path, curdir

config_path = path.join(curdir, 'config', 'default.toml')

def read_config(path = config_path):
    data = {}
    with open(path, 'r') as conf:
        conf.readline()
        org, org_path = conf.readline().split(' = ')
        usr, usr_path = conf.readline().split(' = ')
        ticket, ticket_path = conf.readline().split(' = ')

        for attr in ['org', 'usr', 'ticket']:
            # Store parsed result
            data[locals()[attr]] = locals()[attr + '_path'].strip()[1:-1]

    return data
