from typing import Optional, TypedDict


class GitHubColumnsRequest(TypedDict, total=False):
    '''
    in: path
    '''
    project_id: int
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
