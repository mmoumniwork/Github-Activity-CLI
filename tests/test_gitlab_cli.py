from typing import Dict, List
from src.github_cli import GithubCLI

def test_show_activities() -> None:
    data: List[Dict[str, str]] = [
        {
            "id": 2,
            "type": "WatchEvent",
            "actor": {
                "id": 78799596,
                "login": "Mohamed-Moumni",
                "display_login": "Mohamed-Moumni",
                "gravatar_id": "",
                "url": "https://api.github.com/users/Mohamed-Moumni",
                "avatar_url": "https://avatars.githubusercontent.com/u/78799596?",
            },
            "payload": {
                "repository_id": 672836880,
                "push_id": 19309928585,
                "size": 1,
                "distinct_size": 1,
                "ref": "refs/heads/main",
                "head": "c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                "before": "06bba731d2dcc4ea257a8fd712220b756afa11be",
                "commits": [
                    {
                        "sha": "c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                        "author": {
                            "email": "78799596+Mohamed-Moumni@users.noreply.github.com",
                            "name": "Mohamed Moumni",
                        },
                        "message": "Update README.md",
                        "distinct": True,
                        "url": "https://api.github.com/repos/Mohamed-Moumni/Mohamed-Moumni/commits/c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                    }
                ],
            },
            "repo": {
                "id": 672836880,
                "name": "Mohamed-Moumni/Mohamed-Moumni",
                "url": "https://api.github.com/repos/Mohamed-Moumni/Mohamed-Moumni",
            },
            "created_at": "2024-07-06T12:55:07Z",
        },
        {
            "id": 2,
            "type": "WatchEvent",
            "actor": {
                "id": 78799596,
                "login": "Mohamed-Moumni",
                "display_login": "Mohamed-Moumni",
                "gravatar_id": "",
                "url": "https://api.github.com/users/Mohamed-Moumni",
                "avatar_url": "https://avatars.githubusercontent.com/u/78799596?",
            },
            "payload": {
                "repository_id": 672836880,
                "push_id": 19309928585,
                "size": 1,
                "distinct_size": 1,
                "ref": "refs/heads/main",
                "head": "c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                "before": "06bba731d2dcc4ea257a8fd712220b756afa11be",
                "commits": [
                    {
                        "sha": "c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                        "author": {
                            "email": "78799596+Mohamed-Moumni@users.noreply.github.com",
                            "name": "Mohamed Moumni",
                        },
                        "message": "Update README.md",
                        "distinct": True,
                        "url": "https://api.github.com/repos/Mohamed-Moumni/Mohamed-Moumni/commits/c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                    }
                ],
            },
            "repo": {
                "id": 672836880,
                "name": "Mohamed-Moumni/Mohamed-Moumni",
                "url": "https://api.github.com/repos/Mohamed-Moumni/Mohamed-Moumni",
            },
            "created_at": "2024-07-06T12:55:07Z",
        },
        {
            "id": 2,
            "type": "WatchEvent",
            "actor": {
                "id": 78799596,
                "login": "Mohamed-Moumni",
                "display_login": "Mohamed-Moumni",
                "gravatar_id": "",
                "url": "https://api.github.com/users/Mohamed-Moumni",
                "avatar_url": "https://avatars.githubusercontent.com/u/78799596?",
            },
            "payload": {
                "repository_id": 672836880,
                "push_id": 19309928585,
                "size": 1,
                "distinct_size": 1,
                "ref": "refs/heads/main",
                "head": "c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                "before": "06bba731d2dcc4ea257a8fd712220b756afa11be",
                "commits": [
                    {
                        "sha": "c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                        "author": {
                            "email": "78799596+Mohamed-Moumni@users.noreply.github.com",
                            "name": "Mohamed Moumni",
                        },
                        "message": "Update README.md",
                        "distinct": True,
                        "url": "https://api.github.com/repos/Mohamed-Moumni/Mohamed-Moumni/commits/c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                    }
                ],
            },
            "repo": {
                "id": 672836880,
                "name": "Mohamed-Moumni/Mohamed-Moumni",
                "url": "https://api.github.com/repos/Mohamed-Moumni/Mohamed-Moumni",
            },
            "created_at": "2024-07-06T12:55:07Z",
        },
        {
            "id": 2,
            "type": "WatchEvent",
            "actor": {
                "id": 78799596,
                "login": "Mohamed-Moumni",
                "display_login": "Mohamed-Moumni",
                "gravatar_id": "",
                "url": "https://api.github.com/users/Mohamed-Moumni",
                "avatar_url": "https://avatars.githubusercontent.com/u/78799596?",
            },
            "payload": {
                "repository_id": 672836880,
                "push_id": 19309928585,
                "size": 1,
                "distinct_size": 1,
                "ref": "refs/heads/main",
                "head": "c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                "before": "06bba731d2dcc4ea257a8fd712220b756afa11be",
                "commits": [
                    {
                        "sha": "c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                        "author": {
                            "email": "78799596+Mohamed-Moumni@users.noreply.github.com",
                            "name": "Mohamed Moumni",
                        },
                        "message": "Update README.md",
                        "distinct": True,
                        "url": "https://api.github.com/repos/Mohamed-Moumni/Mohamed-Moumni/commits/c42ef3c25bbef799a7db4e916e0d89b75a82fccd",
                    }
                ],
            },
            "repo": {
                "id": 672836880,
                "name": "Mohamed-Moumni/Mohamed-Moumni",
                "url": "https://api.github.com/repos/Mohamed-Moumni/Mohamed-Moumni",
            },
            "created_at": "2024-07-06T12:55:07Z",
        },
        ]

    github_cli = GithubCLI()
    
    github_cli.show_activities(data)
    
    assert 1 == 1