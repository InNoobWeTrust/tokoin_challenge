from os import PathLike, path, curdir
from typing import Dict

config_path = path.join(curdir, 'config', 'default.toml')

def read_config(path: str or PathLike = config_path) -> Dict[str, str]:
    data = {}
    with open(path, 'r') as conf:
        conf.readline() # Skip line with `[Data]`

        for _ in range(3):
            k, v = conf.readline().split(' = ')
            # Store parsed result
            data[k] = v.strip()[1:-1]

    return data

CONFIG = read_config()
USER_CONFIG_KEY = 'User'
TICKET_CONFIG_KEY = 'Ticket'
ORG_CONFIG_KEY = 'Organization'
