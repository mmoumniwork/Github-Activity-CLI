from github_api import GithubAPI
from typing import Dict, List
from prettytable import PrettyTable


class GithubCLI:
    def __init__(self) -> None:
        pass

    def show_activities(self, data: Dict[str, str], activity_type: str = None) -> None:
        table = PrettyTable()
        table.field_names = ["ID", "TYPE", "ACTOR", "REPO", "CREATED_AT"]
        if activity_type:
            data = list(filter(lambda item: item["type"] == activity_type, data))
        table.add_rows(
            [
                [
                    item["id"],
                    item["type"],
                    item["actor"]["login"],
                    item["repo"]["name"],
                    item["created_at"],
                ]
                for item in data
            ]
        )
        print(table)

    def show_repos(self, data: Dict[str, str]) -> None:
        table = PrettyTable()
        table.field_names = [
            "NAME",
            "DESCRIPTION",
            "URL",
            "DEF_BRANCH",
            "CREATED_AT",
        ]
        table.add_rows(
            [
                [
                    item["name"],
                    item["description"],
                    item["html_url"],
                    item["default_branch"],
                    item["created_at"],
                ]
                for item in data
            ]
        )
        table.max_width["NAME"] = 10
        table.max_width["DESCRIPTION"] = 50
        table.max_width["URL"] = 20
        print(table)
