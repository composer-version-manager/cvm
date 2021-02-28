from argparse import Action, Namespace
from typing import Optional

from colorama import Fore
from cvm.commands.command import Command
from cvm.helpers.cli import info, warning
from cvm.helpers.fs import find_file_in_parent
from cvm.services.application_service import ApplicationService
from cvm.services.composer_service import ComposerService
from cvm.services.config_service import ConfigService
from cvm.services.github_service import GitHubService


class ScanCommand(Command):
    NAME = 'scan'
    DESCRIPTION = 'If present use .cvm_config from the current or specified directory.'

    def exec(self, args: Namespace):
        version = None
        config_file = ConfigService.find()

        if config_file is not None:
            version = self._check_local(config_file)
        else:
            version = self._check_global()

        if version is None:
            return

        github_service = GitHubService('composer', 'composer')
        composer_service = ComposerService(github_service)
        updated_path = composer_service.use_version(version, False)

        if not updated_path:
            return
        
        msg = info(f"Using composer version {version}")

        print(f"export PATH=\"{updated_path}\"; echo \"{msg}\";")

    def _check_local(self, config_file: str) -> Optional[str]:
        data = ConfigService.read(config_file)
        if not ConfigService.validate(data):
            msg = warning(".cvm_config format in current directory is invalid.")
            print(f"echo \"{msg}\"")

            return None

        return data['requires']

    def _check_global(self) -> Optional[str]:
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
