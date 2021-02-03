from typing import Optional, TypedDict


class GitHubProjectsRequest(TypedDict, total=False):
    '''
    in: path
    '''
    org: str
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
