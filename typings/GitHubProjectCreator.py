from typing import TypedDict


class GitHubProjectCreator(TypedDict):
    login: str
    id: int
    avatar_url: str
    url: str
    html_url: str
    type: str
    site_admin: bool
