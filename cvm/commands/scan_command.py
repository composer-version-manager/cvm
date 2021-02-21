from argparse import Action, Namespace

from cvm.commands.command import Command
from cvm.services.composer_service import ComposerService
from cvm.services.config_service import ConfigService
from cvm.services.github_service import GitHubService
from cvm.services.application_service import ApplicationService
from cvm.helpers.cli import warning
from colorama import Fore


class ScanCommand(Command):
    NAME = 'scan'
    DESCRIPTION = 'If present use .cvm_config from the current or specified directory.'

    def exec(self, args: Namespace):
        version = None

        if ConfigService.exists():
            version = self._check_local()
        else:
            version = self._check_global()

        if version is None:
            return

        github_service = GitHubService('composer', 'composer')
        composer_service = ComposerService(github_service)

        updated_path = composer_service.use_version(version, False)

        print(f"export PATH=\"{updated_path}\"; echo Updated path.;")

    def _check_local(self):
        data = ConfigService.read()
        if not ConfigService.validate(data):
            msg = warning(".cvm_config format in current directory is invalid.")
            print(f"echo \"{msg}\"")

            return None

        return data['requires']

    def _check_global(self):
        application_service = ApplicationService()
        
        return application_service.get('global')

    @staticmethod
    def define_signature(parser: Action):
        scan_parser = parser.add_parser(ScanCommand.NAME, help=ScanCommand.DESCRIPTION)
        scan_parser.add_argument(
            'shell',
            nargs=1,
            help='Shell name to cvm within.',
            metavar='{shell}'
        )
