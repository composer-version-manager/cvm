from argparse import Action, Namespace

from cvm.commands.command import Command
from cvm.services.composer_service import ComposerService
from cvm.services.config_service import ConfigService
from cvm.services.github_service import GitHubService


class ScanCommand(Command):
    NAME = 'scan'
    DESCRIPTION = 'If present use .cvm_config from the current or specified directory.'

    def exec(self, args: Namespace):
        if not ConfigService.exists():
            return

        data = ConfigService.read()
        if not ConfigService.validate(data):
            print("echo Invalid cvm config.")

        github_service = GitHubService('composer', 'composer')
        composer_service = ComposerService(github_service)

        install_path = composer_service.use_version(data['requires'])

        print(f"export PATH=:{install_path}:$PATH; echo Updated path.")

    @staticmethod
    def define_signature(parser: Action):
        scan_parser = parser.add_parser(ScanCommand.NAME, help=ScanCommand.DESCRIPTION)
        scan_parser.add_argument(
            'shell',
            nargs=1,
            help='Shell name to cvm within.',
            metavar='{shell}'
        )
