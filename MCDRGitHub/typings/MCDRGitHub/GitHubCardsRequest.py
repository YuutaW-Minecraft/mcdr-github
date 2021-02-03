from .GitHubCardsState import GitHubCardsState
from typing import Optional, TypedDict


class GitHubCardsRequest(TypedDict, total=False):
    '''
    column_id parameter

    in: path
    '''
    column_id: int
    '''
    Filters the project cards that are returned by the card's state. @see GitHubCardsState.

    in: query
    '''
    archived_state: Optional[GitHubCardsState]
    '''
    Results per page (max 100)

    in: query
    '''
    per_page: Optional[int]
    '''
    Page number of the results to fetch.

    in: query
    '''
    page: Optional[int]
