from os import PathLike

from tokoin_challenge.file_ops.peek import peekline
from tokoin_challenge.stream.obj_collector import collect_obj


def obj_streamer(data_path: str):
    with open(data_path, 'r') as f:
        while len(peekline(f)):
            line = f.readline().strip()
            if '{' in line:
                yield collect_obj(f)


