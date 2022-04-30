from argparse import ArgumentParser, Namespace
from typing import Callable, Dict, List
from pytermgui.pretty import print
from tokoin_challenge.config.config import CONFIG, ORG_CONFIG_KEY, TICKET_CONFIG_KEY, USER_CONFIG_KEY
from tokoin_challenge.matcher.obj_deep_search import is_deep_contain, is_field_contain
from tokoin_challenge.search.search_user import fill_org_meta_data, fill_ticket_metadata, fill_user_metadata, search_org_stream, search_ticket_stream, search_user_stream
from tokoin_challenge.stream.data_stream import get_fields


def parse_arguments() -> Namespace:
    """Parse command line arguments"""

    parser = ArgumentParser()
    parser.add_argument('-m', '--mode', help='Search mode', choices=['user', 'ticket', 'organization'], required=True)
    parser.add_argument('-s', '--term', help='Search term')
    parser.add_argument('-f', '--field', help='Field to search for')

    return parser.parse_args()

def search_user(search_term: str, field: str):
    print(f'Searching users with (term: {search_term}, field: {field})...')
    matcher = lambda usr: is_deep_contain(
        usr.data,
        search_term=search_term,
    )

    if field is not None:
        matcher = lambda usr: is_field_contain(
            usr.data,
            field=field, search_term=search_term,
        )

    for usr in search_user_stream(matcher):
        print(fill_user_metadata(usr))

def search_ticket(search_term: str, field: str):
    print(f'Searching tickets with (term: {search_term}, field: {field})...')
    matcher = lambda ticket: is_deep_contain(
        ticket.data,
        search_term=search_term,
    )

    if field is not None:
        matcher = lambda ticket: is_field_contain(
            ticket.data,
            field=field, search_term=search_term,
        )

    for ticket in search_ticket_stream(matcher):
        print(fill_ticket_metadata(ticket))

def search_organization(search_term: str, field: str):
    print(f'Searching organizations with (term: {search_term}, field: {field})...')
    matcher = lambda org: is_deep_contain(
        org.data,
        search_term=search_term,
    )

    if field is not None:
        matcher = lambda org: is_field_contain(
            org.data,
            field=field, search_term=search_term,
        )

    for org in search_org_stream(matcher):
        print(fill_org_meta_data(org))

MODE_CALLBACK: Dict[str, Callable[[str, str], None]] = {
    'user': search_user,
    'ticket': search_ticket,
    'organization': search_organization,
}

DESCRIBE_CALLBACKS: Dict[str, Callable[[], List[str]]] = {
    'user': lambda: get_fields(CONFIG[USER_CONFIG_KEY]),
    'ticket': lambda: get_fields(CONFIG[TICKET_CONFIG_KEY]),
    'organization': lambda: get_fields(CONFIG[ORG_CONFIG_KEY]),
}

def main():
    args = parse_arguments()

    if args.term is None and args.field is None:
        print('Please provide search term!')
        print('For fine grained, you can filter by the specific fields below:')
        print(DESCRIBE_CALLBACKS[args.mode]())
    else:
        MODE_CALLBACK[args.mode](args.term, args.field)
