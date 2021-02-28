import os
import subprocess
from argparse import Action, Namespace

from cvm.commands.command import Command
from cvm.helpers.cli import info
from cvm.services.composer_service import ComposerService
from cvm.services.config_service import ConfigService
from cvm.services.github_service import GitHubService


class UseCommand(Command):
    NAME = 'use'
    DESCRIPTION = 'Globally use a specific composer version.'

    def exec(self, args: Namespace):
        version = args.version[0]

        github_service = GitHubService('composer', 'composer')
        composer_service = ComposerService(github_service)

        composer_service.use_version(version, True)

        print(info(f"Global composer version updated to {version}."))

    @staticmethod
    def define_signature(parser: Action):
        use_parser = parser.add_parser(UseCommand.NAME, help=UseCommand.DESCRIPTION)
        use_parser.add_argument(
            'version',
            nargs=1,
            help='Composer version to use.',
            metavar='{version}'
        )
