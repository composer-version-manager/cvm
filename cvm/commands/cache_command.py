from argparse import Action, Namespace

from cvm.commands.command import Command
from cvm.helpers.cli import info, warning
from cvm.services.cache_service import CacheService
from cvm.services.composer_service import ComposerService
from cvm.services.github_service import GitHubService


class CacheCommand(Command):
    NAME = 'cache:clear'
    DESCRIPTION = 'Clear cached composer tags.'

    def exec(self, args: Namespace):
        try:
            GitHubService.TAGS_FILE_PATH.unlink(missing_ok=True)
        except OSError:
            print(warning("Failed to clear cached tags."))
            return

        print(info("Cached tags successfully cleared."))

    @staticmethod
    def define_signature(parser: Action):
        parser.add_parser(CacheCommand.NAME, help=CacheCommand.DESCRIPTION)
