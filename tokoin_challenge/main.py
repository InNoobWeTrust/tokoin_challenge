from argparse import ArgumentParser, Namespace
from typing import Callable, Dict
from pytermgui.pretty import pprint


def parse_arguments() -> Namespace:
    """Parse command line arguments"""

    parser = ArgumentParser()
    parser.add_argument('-m', '--mode', help='Search mode', choices=['user', 'ticket', 'organization'], required=True)
    parser.add_argument('-s', '--term', help='Search term', required=True)
    parser.add_argument('-f', '--field', help='Field to search for')

    return parser.parse_args()

def search_user(seach_term: str, field: str):
    pprint(f'Searching users with (term: {seach_term}, field: {field})...')

def search_ticket(seach_term: str, field: str):
    pprint(f'Searching tickets with (term: {seach_term}, field: {field})...')

def search_organization(seach_term: str, field: str):
    pprint(f'Searching organizations with (term: {seach_term}, field: {field})...')

MODE_CALLBACK: Dict[str, Callable[[str, str],None]] = {
    'user': search_user,
    'ticket': search_ticket,
    'organization': search_organization,
}

def main():
    args = parse_arguments()
    MODE_CALLBACK[args.mode](args.term, args.field)
