import sys
import os

from cvm.services.cache_service import CacheService
from cvm.services.github_service import GitHubService
import logging


class ComposerService:
    def __init__(self, github_service: GitHubService):
        self.github_service = github_service
        self.tags = None

    def list_tags(self):
        if self.tags is None:
            self.tags = self.github_service.list_tags()

        return self.tags

    def tag_exists(self, desired_tag: str) -> bool:
        github_tags = self.list_tags()

        for tag_object in github_tags:
            if tag_object.get('name') == desired_tag:
                return True

        return False

    @staticmethod
    def cached_version_exists(tag_name: str) -> bool:

        return os.path.exists(CacheService.CACHE_DIR + "/{}".format(tag_name))

    def install_version(self, tag_name: str) -> bool:
        if not self.tag_exists(tag_name):
            logging.error("Tag {} does not exist.".format(tag_name))
            sys.exit(1)

        # TODO: Download version into cache directory

        return True

    def use_version(self, tag_name: str, check_exists: bool = True) -> bool:
        if check_exists and not ComposerService.cached_version_exists(tag_name):
            return False

        # TODO: Use cached version if exists

        return True
