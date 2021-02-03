from MCDRGitHub.GitHub import GitHub
from MCDRGitHub.typings.MCDRGitHub import GitHubCardsState
import unittest
import os

from requests.models import HTTPBasicAuth

class GitHubTestCase(unittest.TestCase):
    gh: GitHub

    def setUp(self) -> None:
        try:
            # Specify the 'GH_USER' and 'GH_TOKEN' environment variable
            # is helpful when you want to test something like 'test_get_project'.
            #
            # GH_USER is your GitHub username, and GH_TOKEN is your personal access token.
            # I've granted the following permission in my test:
            #     admin:org, notifications, repo, user
            self.gh = GitHub(
                HTTPBasicAuth(os.environ["GH_USER"], os.environ["GH_TOKEN"]))
        except KeyError:
            self.gh = GitHub()

    def test_build_uri(self) -> None:
        self.assertEqual(
            self.gh._build_uri('/a'),  # type: ignore
            "https://api.github.com/a",
        )

    def test_rget(self) -> None:
        url = self.gh._build_uri('/users/pan93412')  # type: ignore
        content = self.gh._rget(url).json()  # type: ignore

        self.assertEqual(content["id"], 28441561)

    def test_exception(self) -> None:
        exception = self.gh._exception('a')  # type: ignore

        self.assertEqual(str(exception), "Request failed: a")

    def test_extract_query(self) -> None:
        self.assertEqual(
            self.gh._extract_query(  # type: ignore
                {'a': 3}, ['a', 'b']),
            {
                'a': '3',
            })

        self.assertEqual(
            self.gh._extract_query(  # type: ignore
                {'a': '3'}, ['a', 'b']),
            {
                'a': '3',
            })

        self.assertEqual(
            self.gh._extract_query(  # type: ignore
                {
                    'a': '3',
                    'b': 2
                }, ['a', 'b']),
            {
                'a': '3',
                'b': '2'
            })

        self.assertEqual(
            self.gh._extract_query(  # type: ignore
                {'c': 'none'}, ['a', 'b']),
            {})

        self.assertEqual(
            self.gh._extract_query(  # type: ignore
                {'c': GitHubCardsState.ARCHIVED}, ['c']),
            {'c': 'archived'})

    def test_get_user(self) -> None:
        user = self.gh.get_user('pan93412')

        self.assertEqual(user["id"], 28441561)

    def test_get_user_failed(self) -> None:
        self.assertRaises(
            Exception,
            lambda: self.gh.get_user('efbvlijercjiedclndckwdlferldaaaaa'))

    def test_list_projects(self) -> None:
        projects = self.gh.list_projects({"org": "YuutaW-Minecraft"})

        self.assertGreaterEqual(len(projects), 1)

    def test_list_projects_failed(self) -> None:
        self.assertRaises(
            Exception, lambda: self.gh.list_projects(
                {"org": "YuutaW-MinecraftAAAAAAAAAA"}))

    def test_get_project(self) -> None:
        project = self.gh.get_project({"project_id": 11425566})

        self.assertEqual(project["id"], 11425566)

    def test_get_project_failed(self) -> None:
        self.assertRaises(Exception,
                          lambda: self.gh.get_project({"project_id": -1}))

    def test_list_columns(self) -> None:
        columns = self.gh.list_columns({"project_id": 11425566})

        self.assertGreaterEqual(len(columns), 1)

    def test_list_columns_failed(self) -> None:
        self.assertRaises(Exception,
                          lambda: self.gh.list_columns({"project_id": -1}))

    def test_get_column(self) -> None:
        column = self.gh.get_column({"column_id": 12755884})

        self.assertEqual(column["id"], 12755884)

    def test_get_column_failed(self) -> None:
        self.assertRaises(Exception,
                          lambda: self.gh.get_column({"column_id": -1}))

    def test_list_cards(self) -> None:
        cards = self.gh.list_cards({"column_id": 12755884})

        self.assertGreaterEqual(len(cards), 1)

    def test_list_archived_cards(self) -> None:
        cards = self.gh.list_cards({
            "column_id": 12755884,
            "archived_state": GitHubCardsState.ARCHIVED
        })

        self.assertEqual(len(cards), 0)

    def test_list_cards_failed(self) -> None:
        self.assertRaises(Exception,
                          lambda: self.gh.list_cards({"column_id": -1}))

    def test_get_card(self) -> None:
        card = self.gh.get_card({"card_id": 54127373})

        self.assertEqual(card["id"], 54127373)

    def test_get_card_failed(self) -> None:
        self.assertRaises(Exception, lambda: self.gh.get_card({"card_id": -1}))
