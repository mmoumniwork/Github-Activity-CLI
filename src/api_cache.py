import time
from datetime import datetime
from typing import Any, Callable
import urllib.request
from urllib.error import HTTPError
import logging
import json

CACHE_MAX_TIME = 180
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def call_command(type: str, username: str, data: Any, method: Callable):
    user_item = list(filter(lambda item: item["username"] == username, data))
    user_item = None if not user_item else user_item[0]
    if user_item:
        print("not new")
        if user_item[type]["data"]:
            cache_timestamp = datetime.now() - user_item[type]["last_update"]
            if cache_timestamp.seconds >= CACHE_MAX_TIME:
                print("run out of cache")
                user_item[type].update("data", method(username))
                user_item[type].update("last_update", datetime.now())
                return user_item[type]["data"]
            else:
                print("user cache")
                return user_item[type]["data"]
        else:
            print("create it")
            user_data = method(username)
            user_item[type].update("data", user_data)
            user_item[type].update("last_update", datetime.now())
            return user_item[type]["data"]
    else:
        print("new")
        user_data = method(username)
        new_user = {
            "username": username,
            type: {
                "data": user_data,
                "last_update": datetime.now(),
            },
        }
        data.append(new_user)
        return new_user[type]["data"]


class api:
    @staticmethod
    def fetch(type):
        def decorator(func):
            data = []

            def wrapper(self, *args, **kwargs):
                username = self.username[0]
                match type:
                    case "activity":
                        return call_command(
                            type, username, data, api.get_user_activities
                        )
                    case "repos":
                        return call_command(
                            type, username, data, api.get_the_user_repos
                        )

            return wrapper

        return decorator

    @staticmethod
    def fetch_url(url: str) -> Any:
        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode("utf-8"))
                return data
        except (Exception, HTTPError) as e:
            logger.error(f"fetch url error: {e}", exc_info=True)

    @staticmethod
    def get_user_activities(username: str):
        try:
            data = api.fetch_url(
                f"https://api.github.com/users/{username}/events/public"
            )
            return data
        except Exception as e:
            logger.error(f"get use activites error: {e}", exc_info=True)

    @staticmethod
    def get_the_user_repos(username: str) -> Any:
        try:
            data = api.fetch_url(f"https://api.github.com/users/{username}/repos")
            return data
        except Exception as e:
            logger.error(f"get user repos error: {e}", exc_info=True)
