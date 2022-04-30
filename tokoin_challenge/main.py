from argparse import ArgumentParser, Namespace
from typing import Callable, Dict
from pytermgui.pretty import print
from tokoin_challenge.matcher.obj_deep_search import is_deep_contain, is_field_contain
from tokoin_challenge.search.search_user import fill_user_metadata, search_user_stream


def parse_arguments() -> Namespace:
    """Parse command line arguments"""

    parser = ArgumentParser()
    parser.add_argument('-m', '--mode', help='Search mode', choices=['user', 'ticket', 'organization'], required=True)
    parser.add_argument('-s', '--term', help='Search term', required=True)
    parser.add_argument('-f', '--field', help='Field to search for')

    return parser.parse_args()

def search_user(seach_term: str, field: str):
    print(f'Searching users with (term: {seach_term}, field: {field})...')

    for usr in search_user_stream(lambda usr: is_field_contain(usr.data, field=field, search_term=seach_term)):
        print(usr)
        print(f'With metadata:\n{fill_user_metadata(usr)}')

def search_ticket(seach_term: str, field: str):
    print(f'Searching tickets with (term: {seach_term}, field: {field})...')

def search_organization(seach_term: str, field: str):
    print(f'Searching organizations with (term: {seach_term}, field: {field})...')

MODE_CALLBACK: Dict[str, Callable[[str, str],None]] = {
    'user': search_user,
    'ticket': search_ticket,
    'organization': search_organization,
}

def main():
    args = parse_arguments()
    MODE_CALLBACK[args.mode](args.term, args.field)
