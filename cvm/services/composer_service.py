import logging
import pathlib
import subprocess
import sys

import requests

from cvm.services.cache_service import CacheService
from cvm.services.github_service import GitHubService


class ComposerService:
    SETUP_URL = 'https://getcomposer.org/installer'
    SETUP_FILENAME = 'composer-setup.php'

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
        '''
        Check if the local cache holds the requested version
        :param tag_name: The version to check
        :return: Bool
        '''

        cache_path = CacheService.CACHE_DIR / tag_name / 'composer'
        return cache_path.exists()

    def _get_setup_path(self) -> pathlib.Path:
        '''
        Download and return the path to the composer setup file.
        Will call sys.exit(1) if the composer setup file is unreachable
        '''
        setup_path = CacheService.SETUP_DIR / self.SETUP_FILENAME
        if not setup_path.exists():
            r = requests.get(self.SETUP_URL)
            if not r.ok:
                logging.error(f"Could not download the composer setup file. \n {r.content}")
                sys.exit(1)
            setup_path.write_bytes(r.content)
        return setup_path

    def install_version(self, tag_name: str, quiet=False) -> pathlib.Path:
        if not self.tag_exists(tag_name):
            logging.error("Tag {} does not exist.".format(tag_name))
            sys.exit(1)

        setup_path = self._get_setup_path()
        cache_path = CacheService.make_cache_folder(tag_name)

        if ComposerService.cached_version_exists(tag_name):
            return cache_path

        cmd = ['php', str(setup_path), f'--install-dir={str(cache_path)}', '--filename=composer', f'--version={tag_name}']
        result = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
        if not quiet:
            print(result.stdout.decode('utf-8'))

        return cache_path

    def use_version(self, tag_name: str) -> str:
        install_path = self.install_version(tag_name, quiet=True)

        return str(install_path)
