from typing import Dict, Iterator, List

from tokoin_challenge.file_ops.peek import peekline
from tokoin_challenge.stream.obj_collector import collect_obj


def obj_streamer(data_path: str) -> Iterator[Dict]:
    with open(data_path, 'r') as f:
        while len(peekline(f)):
            line = f.readline().strip()

            if '{' in line:
                yield collect_obj(f)


def get_fields(data_path: str) -> List[str]:
    obj: Dict = next(
        obj_streamer(data_path))  # We know this is absolutely a dict

    return list(obj.keys())


def get_filterable_fields(data_path: str) -> List[str]:
    obj: Dict = next(
        obj_streamer(data_path))  # We know this is absolutely a dict

    return [
        key for key, value in obj.items()
        if isinstance(value, int) or isinstance(value, bool)
    ]


def get_searchable_fields(data_path: str) -> List[str]:
    obj: Dict = next(
        obj_streamer(data_path))  # We know this is absolutely a dict

    return [
        key for key, value in obj.items()
        if not isinstance(value, int) and not isinstance(value, bool)
    ]
