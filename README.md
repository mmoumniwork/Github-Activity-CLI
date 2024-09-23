# GitHub Activity CLI

GitHub Activity CLI is a simple command-line interface tool that allows you to fetch and display recent GitHub activities and repositories for a specified user.

## Features

- Connect to a GitHub account
- Display recent GitHub activities
- Filter activities by type
- Show user repositories
- Disconnect from the GitHub account

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/github-activity-cli.git
   cd github-activity-cli
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the CLI by executing the `main.py` file:

```
python main.py
```

### Available Commands

1. **Connect to a GitHub account**
   ```
   connect <username>
   ```
   Example: `connect octocat`

2. **Show recent activities**
   ```
   activity [activity_type]
   ```
   Example: `activity` (shows all activities)
   Example: `activity PushEvent` (shows only push events)

3. **Show user repositories**
   ```
   repos
   ```

4. **Disconnect from the GitHub account**
   ```
   disconnect
   ```

5. **Exit the CLI**
   Use Ctrl+C or close the terminal

## Example Session

```
github-activity-cli: connect octocat
github-activity-cli: activity
[Table displaying recent activities]
github-activity-cli: activity PushEvent
[Table displaying recent push events]
github-activity-cli: repos
[Table displaying repositories]
github-activity-cli: disconnect
github-activity-cli: 
```

## Project Structure

- `main.py`: Entry point of the application
- `parser.py`: Handles command-line argument parsing
- `github_api.py`: Manages GitHub API interactions
- `github_cli.py`: Contains the CLI display logic
- `api_cache.py`: Implements caching for API requests

## Notes

- The CLI uses a simple caching mechanism to reduce API calls. Cached data expires after 3 minutes.
- Make sure you have a stable internet connection to fetch data from GitHub.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

### This Project is part of Challanges of Roadmap.sh
https://roadmap.sh/projects/github-user-activity