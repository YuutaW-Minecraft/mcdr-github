from typing import TypedDict


class GitHubUserInfo(TypedDict):
    login: str
    id: str
    name: str
    url: str
    html_url: str
    avatar_url: str
    bio: str