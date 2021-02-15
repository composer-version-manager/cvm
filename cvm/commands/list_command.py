from argparse import Action, Namespace

from cvm.commands.command import Command
from cvm.services.cache_service import CacheService
from cvm.services.composer_service import ComposerService
from cvm.services.github_service import GitHubService


class ListCommand(Command):
    NAME = 'list'
    DESCRIPTION = 'Print a list of composer versions'

    def exec(self, args: Namespace):
        github_service = GitHubService('composer', 'composer')
        composer_service = ComposerService(github_service)
        installed = [i.name for i in CacheService.CACHE_DIR.iterdir()]

        for tag in composer_service.list_tags():
            if tag['name'] in installed:
                print(f"* {tag['name']} (installed)")
            else:
                print(f"* {tag['name']}")

    @staticmethod
    def define_signature(parser: Action):
        parser.add_parser(ListCommand.NAME, help=ListCommand.DESCRIPTION)
