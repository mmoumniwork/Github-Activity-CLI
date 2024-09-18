RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def main() -> None:
    while True:
        github_cli_input = input(f"{GREEN}github-activity-cli: {RESET}")
        github_cli_input = github_cli_input.split(' ')

if __name__ == "__main__":
    main()
