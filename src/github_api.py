from typing import Any
from urllib.error import HTTPError
from api_cache import api
import urllib.request
import json
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


class GithubAPI:
    def __init__(self, username: str) -> None:
        self.username = username

    def disconnect(self):
        self.username = None

    def connect(self, username: str):
        self.username = username

    @api.fetch("activity")
    def get_user_activities(self) -> Any:
        pass

    @api.fetch("repos")
    def get_the_user_repos(self) -> Any:
        pass
