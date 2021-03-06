from typing import Callable, Iterator
from tokoin_challenge.config.config import CONFIG, ORG_CONFIG_KEY, TICKET_CONFIG_KEY, USER_CONFIG_KEY, read_config
from tokoin_challenge.model.organization import Organization
from tokoin_challenge.model.ticket import Ticket
from tokoin_challenge.model.user import User
from tokoin_challenge.stream.data_stream import obj_streamer

USER_STREAM_KEY = 'user'
TICKET_STREAM_KEY = 'ticket'
ORG_STREAM_KEY = 'org'

SUBMITTER_ID_KEY = 'submitter_id'
ASSIGNEE_ID_KEY = 'assignee_id'
SUBJECT_KEY = 'subject'
NAME_KEY = 'name'

STREAM_PROVIDERS = {
    USER_STREAM_KEY:
    lambda: map(
        lambda data: User(data),
        obj_streamer(CONFIG[USER_CONFIG_KEY]),
    ),
    TICKET_STREAM_KEY:
    lambda: map(
        lambda data: Ticket(data),
        obj_streamer(CONFIG[TICKET_CONFIG_KEY]),
    ),
    ORG_STREAM_KEY:
    lambda: map(
        lambda data: Organization(data),
        obj_streamer(CONFIG[ORG_CONFIG_KEY]),
    ),
}


def search_user_stream(matcher: Callable[[User], bool]) -> Iterator[User]:
    '''
    Search users by filtering object stream with string fields
    '''

    return filter(
        lambda usr: matcher(usr),
        STREAM_PROVIDERS[USER_STREAM_KEY](),
    )


def fill_user_metadata(usr: User) -> User:
    if usr.org_ref is not None:
        for org in STREAM_PROVIDERS[ORG_STREAM_KEY]():
            '''
            Find single organization that the user belongs to
            '''

            if org.id == usr.org_ref:
                usr.set_org_name(org.data[NAME_KEY])

                break

    for ticket in STREAM_PROVIDERS[TICKET_STREAM_KEY]():
        '''
        Find related tickets
        Multiple tickets, so bottle neck happens here

        Note: Ticket may not have submitter or assignee
        '''

        if ticket.data.get(SUBMITTER_ID_KEY) == usr.id:
            usr.add_submitted_ticket(ticket.data[SUBJECT_KEY])

        if ticket.data.get(ASSIGNEE_ID_KEY) == usr.id:
            usr.add_assigned_ticket(ticket.data[SUBJECT_KEY])

    return usr


def search_ticket_stream(
        matcher: Callable[[Ticket], bool]) -> Iterator[Ticket]:
    '''
    Search tickets by filtering object stream with string fields
    '''

    return filter(
        lambda ticket: matcher(ticket),
        STREAM_PROVIDERS[TICKET_STREAM_KEY](),
    )


def fill_ticket_metadata(ticket: Ticket) -> Ticket:
    for usr in STREAM_PROVIDERS[USER_STREAM_KEY]():
        if ticket.is_submitter_set and ticket.is_assignee_set:
            # Only 1 submitter and 1 assignee

            break

        if ticket.submitter_ref is not None and ticket.submitter_ref == usr.id:
            ticket.set_submitter_name(usr.name)

        if ticket.assignee_ref is not None and ticket.assignee_ref == usr.id:
            ticket.set_assignee_name(usr.name)

    if ticket.org_ref is not None:
        for org in STREAM_PROVIDERS[ORG_STREAM_KEY]():
            if org.id == ticket.org_ref:
                # Only 1 organization
                ticket.set_org_name(org.name)

                break

    return ticket


def search_org_stream(
        matcher: Callable[[Organization], bool]) -> Iterator[Organization]:
    '''
    Search organizations by filtering object stream with string fields
    '''

    return filter(
        lambda org: matcher(org),
        STREAM_PROVIDERS[ORG_STREAM_KEY](),
    )


def fill_org_meta_data(org: Organization) -> Organization:
    for usr in STREAM_PROVIDERS[USER_STREAM_KEY]():
        '''
        Find users belong to the organization
        Multiple users, so bottle neck happens here
        '''

        if usr.org_ref == org.id:
            org.add_user_name(usr.name)

    for ticket in STREAM_PROVIDERS[TICKET_STREAM_KEY]():
        '''
        Find tickets belong to the organization
        Multiple tickets, so bottle neck happens here
        '''

        if ticket.org_ref == org.id:
            org.add_ticket_subject(ticket.subject)

    return org
