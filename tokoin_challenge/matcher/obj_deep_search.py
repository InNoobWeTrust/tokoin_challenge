from typing import Dict, List, Union

def _is_value_type(value) -> bool:
    return isinstance(value, str) or isinstance(value, int) or isinstance(value, bool)

def is_deep_contain(obj: Union[Dict, List], search_term: Union[str, int, bool]) -> bool:
    '''
    Recursively searching for values that match searchTerm
    '''
    values = list(obj.values()) if isinstance(obj, dict) else obj
    for v in values:
        if _is_value_type(v):
            print(f'checking: {v} - {search_term}')
            if v == search_term:
                print(f'Found!')
                return True
        else:
            if is_deep_contain(v, search_term):
                return True

    return False

def is_field_contain(obj: Dict, field: str, search_term: Union[str, int, bool]) -> bool:
    '''
    Find object whose specified field match search_term
    '''
    for k, v in obj.items():
        print(f'checking: ({k}: {v}) == "{search_term}"?')
        if k == field and v == search_term:
            print(f'Found!')
            return True
    return False
