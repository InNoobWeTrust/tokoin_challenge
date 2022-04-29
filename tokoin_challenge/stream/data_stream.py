from os import PathLike
from typing import Dict, List

from tokoin_challenge.file_ops.peek import peekline
from tokoin_challenge.stream.obj_collector import collect_obj


def obj_streamer(data_path: str):
    with open(data_path, 'r') as f:
        while len(peekline(f)):
            line = f.readline().strip()
            if '{' in line:
                yield collect_obj(f)

def get_fields(data_path: str) -> List[str]:
    obj: Dict = next(obj_streamer(data_path)) # We know this is absolutely a dict
    return list(obj.keys())
