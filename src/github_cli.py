from github_api import GithubAPI


class GithubCLI:
    def __init__(self, user: str) -> None:
        self.user = user
        self.connect()

    def connect(self) -> bool:
        self.github_api = GithubAPI(self.user)
        if self.github_api.get_user(self.user) != None:
            return True
        return False
    
    def show_activities(self):
        pass

    def show_repos(self):
        pass
