from typing import Any, Dict, cast
from requests.models import Response
from MCDRGitHub.typings.MCDRGitHub import GitHubUserInfo, GitHubProjectInfo, GitHubProjectsRequest, GitHubColumnInfo, GitHubColumnsRequest, GitHubColumnRequest, GitHubCardRequest, GitHubCardInfo, GitHubCardsRequest, GitHubProjectRequest
import requests


class GitHub:
    api_root: str
    auth: Any

    def __init__(self, auth: Any = None):
        self.api_root = "https://api.github.com"
        self.auth = auth

    def _build_uri(self, method: str) -> str:
        return f"{self.api_root}{method}"

    def _rget(self, url: str, headers: Dict[str, str] = {}, params: Dict[str, str] = {}) -> Response:
        return requests.get(url, headers=headers, # type: ignore
                            auth=self.auth,
                            params=params)

    def _rget_inertia_preview(self,
                              url: str,
                              headers: Dict[str, str] = {},
                              params: Dict[str, str] = {}) -> Response:
        send_header = {"Accept": "application/vnd.github.inertia-preview+json"}

        send_header.update(headers)

        return self._rget(url, send_header, params)

    def _exception(self, text: str) -> Exception:
        return Exception(f"Request failed: {text}")

    def _return_or_throw(self, r: Response) -> Any:
        if r.status_code == 200:
            return r.json()  # type: ignore
        else:
            raise self._exception(r.text)

    def _extract_query(self, request: object, to_extract: list[str]) -> Dict[str, str]:
        request = cast(Dict[str, Any], request)

        query = {}

        for i in to_extract:
            extracted = request.get(i, None)
            if extracted:
                query[i] = str(extracted)
 
        return query

    def get_user(self, id: str) -> GitHubUserInfo:
        r = self._rget(self._build_uri(f'/users/{id}'))
        return self._return_or_throw(r)

    def list_projects(
            self, request: GitHubProjectsRequest) -> list[GitHubProjectInfo]:
        r = self._rget_inertia_preview(
            self._build_uri(f'/orgs/{request["org"]}/projects'),
            params=self._extract_query(request, ['per_page', 'page']))
        return self._return_or_throw(r)

    def get_project(self, request: GitHubProjectRequest) -> GitHubProjectInfo:
        r = self._rget_inertia_preview(
            self._build_uri(f'/projects/{request["project_id"]}'))
        return self._return_or_throw(r)

    def list_columns(self,
                     request: GitHubColumnsRequest) -> list[GitHubColumnInfo]:
        r = self._rget_inertia_preview(
            self._build_uri(f'/projects/{request["project_id"]}/columns'),
            params=self._extract_query(request, ['per_page', 'page']))
        return self._return_or_throw(r)

    def get_column(self, request: GitHubColumnRequest) -> GitHubColumnInfo:
        r = self._rget_inertia_preview(
            self._build_uri(f'/projects/columns/{request["column_id"]}'))
        return self._return_or_throw(r)

    def list_cards(self, request: GitHubCardsRequest) -> list[GitHubCardInfo]:
        r = self._rget_inertia_preview(
            self._build_uri(f'/projects/columns/{request["column_id"]}/cards'),
            params=self._extract_query(request, ['archived_state', 'per_page', 'page']))
        return self._return_or_throw(r)

    def get_card(self, request: GitHubCardRequest) -> GitHubCardInfo:
        r = self._rget_inertia_preview(
            self._build_uri(f'/projects/columns/cards/{request["card_id"]}'))
        return self._return_or_throw(r)
