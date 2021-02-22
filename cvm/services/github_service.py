import logging
import sys
from typing import Generator

import requests


class GitHubService:
    def __init__(self, owner_id: str, repo_id: str):
        self.owner_id = owner_id
        self.repo_id = repo_id

    def list_tags(self) -> Generator[object]:

        page = 1
        headers = {'Accept': 'application/vnd.github.v3+json'}
        while True:

            url = f"https://api.github.com/repos/{self.owner_id}/{self.repo_id}/tags?page={page}"
            r = requests.get(url, headers=headers)

            if not r.ok:
                logging.error('Failed to fetch available tags from GitHub.')
                sys.exit(1)

            json = r.json()
            if not json:
                return

            for i in json:
                yield i
            page += 1

