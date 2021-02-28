import json
import logging
import sys
from typing import Generator

import requests
from cvm.services.application_service import ApplicationService


class GitHubService:
    TAGS_FILE_PATH = ApplicationService.APP_DIR / 'tags.json'

    def __init__(self, owner_id: str, repo_id: str):
        self.owner_id = owner_id
        self.repo_id = repo_id

    def _fetch_tags(self) -> Generator[object, None, None]:
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

    def list_tags(self) -> Generator[object, None, None]:
        if GitHubService.TAGS_FILE_PATH.exists():
            cache = json.load(GitHubService.TAGS_FILE_PATH.open('r'))
            tags = cache["tags"]

            for tag in tags:
                yield tag
        else:
            tags = []
            for tag in self._fetch_tags():
                tags.append(tag)
                yield tag
            
            cache = {
                "tags": tags
            }
            GitHubService.TAGS_FILE_PATH.write_text(json.dumps(cache))
