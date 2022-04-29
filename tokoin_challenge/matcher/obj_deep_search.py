from typing import Dict, List, Union

def _is_value_type(value) -> bool:
    return isinstance(value, str) or isinstance(value, int) or isinstance(value, bool)

def is_deep_contain(obj: Union[Dict, List], searchTerm: Union[str, int, bool]) -> bool:
    '''
    Recursively searching for values that match searchTerm
    '''
    values = list(obj.values()) if isinstance(obj, dict) else obj
    for v in values:
        if _is_value_type(v):
            print(f'checking: {v} - {searchTerm}')
            if v == searchTerm:
                print(f'Found!')
                return True
        else:
            if is_deep_contain(v, searchTerm):
                return True

    return False
