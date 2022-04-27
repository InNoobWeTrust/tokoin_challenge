from io import TextIOWrapper
from os import wait
from typing import Dict, List, Union

from tokoin_challenge.file_ops.peek import peekline


def value_parser(value: str) -> Union[str, int, bool]:
    res = value
    if res[-1] == ',':
        res = res[:-1]
    if '"' in res:
        return res.replace(r'"', '')
    elif res.isdigit():
        return int(res)
    elif res == 'true':
        return True
    elif res == 'false':
        return False
    raise Exception(f'Value parsing exception: {res}')

BRACKET_PAIRS = {
    '{': '}',
    '[': ']',
}

def collect_obj(file_handle: TextIOWrapper, terminator: str = '}') -> Union[Dict, List]:
    obj: Union[Dict,List] = {} if terminator == '}' else []
    while terminator not in peekline(file_handle) and len(peekline(file_handle)):
        line = file_handle.readline().strip()
        segments = line.split(': ')
        try:
            if isinstance(obj, dict):
                k, v = [value_parser(segment) for segment in segments]
                obj[k] = v
            else:
                obj.append(value_parser(segments[0]))
        except Exception as e:
            if isinstance(obj, dict):
                k, v = value_parser(segments[0]), segments[1]
                obj[k] = collect_obj(file_handle, terminator=BRACKET_PAIRS[v])
            else:
                raise e
    # Encounter closing bracket, advance 1 line to pass the bracket
    _terminate_line = file_handle.readline()
    return obj
