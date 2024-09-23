# import logging
# from src.github_api import GithubAPI


# def test_fetch_url() -> None:
#     urls = [
#         "https://api.github.com/users/Mohamed-Moumni/repos",
#         "https://api.github.com/users/Joknaa/repos",
#         "https://api.github.com/users/Charles-Chrismann/repos",
#     ]
#     github_api = GithubAPI("username_test")
#     for url in urls:
#         assert github_api.fetch_url(url) != None


# def test_invalid_fetch_urls(caplog) -> None:
#     github_api = GithubAPI("username_test")
#     caplog.set_level(logging.ERROR)
#     url = "https://api.github.com/users/sfljsfs/repos"
#     github_api.fetch_url(url)
#     assert "fetch url error:" in caplog.text


# def test_get_valid_user_activities() -> None:
#     github_api = GithubAPI("Mohamed-Moumni")
#     assert github_api.get_user_activities() != None

# def test_get_non_valid_user_activities() -> None:
#     github_api = GithubAPI("sfjlskfj")
#     assert github_api.get_user_activities() == None

# def test_get_the_user_repos() -> None:
#     github_api = GithubAPI("Mohamed-Moumni")
#     assert github_api.get_user_activities() != None

# def test_get_non_the_user_repos() -> None:
#     github_api = GithubAPI("sfjlskfj")
#     assert github_api.get_user_activities() == None

# def test_get_user_activity_by_valid_event_type() -> None:
#     github_api = GithubAPI("Mohamed-Moumni")
#     assert github_api.get_user_activity_by_event_type("PushEvent") != None

# # def test_get_user_activity_by_non_valid_event_type(caplog) -> None:
# #     github_api = GithubAPI("Mohamed-Moumni")
# #     caplog.set_level(logging.ERROR)
# #     github_api.get_user_activity_by_event_type("sfljls")
# #     assert "get user activity by event type error:" in caplog.text

# # def test_get_non_user_activity_by_event_type(caplog) -> None:
# #     github_api = GithubAPI("sdfsfsf")
# #     caplog.set_level(logging.ERROR)
# #     assert "get user activity by event type error:" in caplog.text
