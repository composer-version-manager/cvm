from argparse import Action, Namespace

from cvm.commands.command import Command
from cvm.services.composer_service import ComposerService
from cvm.services.github_service import GitHubService


class UseCommand(Command):
    NAME = 'use'
    DESCRIPTION = 'Use a specific version of Composer; Defaulting to the latest stable major version when there is a ' \
                  'lack of specificity (ie. 2). '

    def exec(self, args: Namespace):
        desired_version = args.version[0]

        github_service = GitHubService('composer', 'composer')
        composer_service = ComposerService(github_service)

        existed = composer_service.use_version(desired_version)
        if not existed:
            composer_service.install_version(desired_version)
            composer_service.use_version(desired_version, False)

    @staticmethod
    def define_signature(parser: Action):
        use_parser = parser.add_parser(UseCommand.NAME, help=UseCommand.DESCRIPTION)
        use_parser.add_argument(
            'version',
            nargs=1,
            help='Composer version to use.',
            metavar='{version}'
        )
