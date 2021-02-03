from typing import TypedDict


class GitHubColumnInfo(TypedDict):
    url: str
    project_url: str
    cards_url: str
    id: int
    name: str
    created_at: str  # todo: a standard date format
    updated_at: str
