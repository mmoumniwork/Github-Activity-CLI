import argparse
from typing import List
from github_api import GithubAPI
from github_cli import GithubCLI


class MyArgumentParser(argparse.ArgumentParser):
    def exit(self, status=0, message=None):
        pass


class Parser:
    def __init__(self) -> None:
        self.githubApi = GithubAPI(None)

    def start(self, cmd_input: List[str]):
        self.parser = MyArgumentParser(
            description="Simple command line interface (CLI) to fetch the recent activity of a GitHub user and display it in the terminal.",
            exit_on_error=False,
        )

        subparsers = self.parser.add_subparsers(
            dest="command", help="Available Commands"
        )
        ## Connect Parser
        connect_parser = subparsers.add_parser(
            "connect", help="Connect with a username"
        )
        connect_parser.add_argument("username", nargs=1, help="Github username")

        ## Disconnect Parser
        disconnect_parser = subparsers.add_parser(
            "disconnect", help="Disconnect from the Github CLI."
        )

        ## Activity Parser
        activity_parser = subparsers.add_parser(
            "activity", help="Show all the your recent activities on Github."
        )
        activity_parser.add_argument(
            "activity_type",
            nargs="?",
            help="Filter Your activities by type",
        )

        subparsers.add_parser("repos", help="Show you Github Repositories.")
        args = self.parser.parse_args(cmd_input)
        self.handle_params(args)

    def handle_params(self, args):
        gitHubCLI = GithubCLI()
        match args.command:
            case "connect":
                self.githubApi.connect(args.username)
            case "activity":
                if self.githubApi.username:
                    data = self.githubApi.get_user_activities()
                    gitHubCLI.show_activities(data, activity_type=args.activity_type)
            case "repos":
                data = self.githubApi.get_the_user_repos()
                gitHubCLI.show_repos(data)
            case "disconnect":
                if self.githubApi.username:
                    self.githubApi.disconnect()
