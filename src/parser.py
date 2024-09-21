import argparse
from typing import List


class MyArgumentParser(argparse.ArgumentParser):
    def exit(self, status=0, message=None):
        pass


class Parser:
    def __init__(self) -> None:
        pass

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
        connect_parser.add_argument("<username>", nargs=1, help="Github username")

        ## Activity Parser
        activity_parser = subparsers.add_parser(
            "activity", help="Show all the your recent activities on Github."
        )
        activity_parser.add_argument(
            "<activity_type>",
            nargs="?",
            help="Filter Your activities by type",
        )

        subparsers.add_parser("repos", help="Show you Github Repositories.")
        args = self.parser.parse_args(cmd_input)
