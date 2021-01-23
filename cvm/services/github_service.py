import logging
import sys

import requests


class GitHubService:
    def __init__(self, owner_id: str, repo_id: str):
        self.owner_id = owner_id
        self.repo_id = repo_id

    def list_tags(self) -> requests.Response:
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(
            "https://api.github.com/repos/{}/{}/tags".format(self.owner_id, self.repo_id),
            headers=headers
        )

        if r.status_code >= 400:
            logging.error('Failed to fetch available tags from GitHub.')
            sys.exit(1)

        json = r.json()

        return json
