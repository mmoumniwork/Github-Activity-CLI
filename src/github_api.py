## things to do
## 1.  fetch users activity

from typing import Any
import urllib.request
from urllib.error import HTTPError
import json
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


class GithubAPI:
    def __init__(self, username: str) -> None:
        self.username = username

    @staticmethod
    def fetch_url(url: str) -> Any:
        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode("utf-8"))
                return data
        except (Exception, HTTPError) as e:
            logger.error(f"fetch url error: {e}", exc_info=True)

    def get_user(self, username) -> Any:
        try:
            user_data = GithubAPI.fetch_url(f"https://api.github.com/users/{username}")
            return user_data
        except (Exception, HTTPError) as e:
            logger.error(f"get user error: {e}", exc_info=True)

    def get_user_activities(self) -> Any:
        try:
            data = GithubAPI.fetch_url(
                f"https://api.github.com/users/{self.username}/events/public"
            )
            return data
        except Exception as e:
            logger.error(f"get user activity error: {e}", exc_info=True)

    def get_the_user_repos(self) -> Any:
        try:
            data = GithubAPI.fetch_url(
                f"https://api.github.com/users/{self.username}/repos"
            )
            return data
        except Exception as e:
            logger.error(f"get user repos error: {e}", exc_info=True)

    def get_user_activity_by_event_type(self, event_type: str) -> Any:
        try:
            data = GithubAPI.fetch_url(
                f"https://api.github.com/users/{self.username}/events/public"
            )
            data = list(filter(lambda item: item["type"] == event_type, data))
            return data
        except Exception as e:
            logger.error(f"get user activity by event type error: {e}", exc_info=True)
