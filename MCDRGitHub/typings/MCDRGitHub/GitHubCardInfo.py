from .GitHubProjectCreator import GitHubProjectCreator
from typing import TypedDict


class GitHubCardInfo(TypedDict):
    url: str
    id: int
    note: str
    creator: GitHubProjectCreator
    created_at: str  # todo: a standard date format
    updated_at: str
    archived: bool
    column_url: str
    content_url: str
    project_url: str
