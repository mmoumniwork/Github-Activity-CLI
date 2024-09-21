from parser import Parser
import logging

logger = logging.getLogger()

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def main() -> None:
    parser = Parser()
    while True:
        try:
            github_cli_input = input(f"{GREEN}github-activity-cli: {RESET}")
            github_cli_input = github_cli_input.split(" ")
            parser.start(github_cli_input)
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    main()
