from .GitHubProjectCreator import GitHubProjectCreator
from typing import TypedDict


class GitHubProjectInfo(TypedDict):
    owner_url: str
    url: str
    html_url: str
    columns_url: str
    id: int
    name: str
    body: str
    number: int
    state: str  # todo: enum
    creator: GitHubProjectCreator
    created_at: str  # todo: a standard date format
    updated_at: str
