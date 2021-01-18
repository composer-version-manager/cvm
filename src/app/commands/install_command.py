from argparse import Action

from src.app.commands.command import Command


class InstallCommand(Command):
    NAME = 'install'

    def exec(self):
        print("Install command executed.")

    @staticmethod
    def define_signature(parser: Action):
        install_parser = parser.add_parser(
            InstallCommand.NAME,
            help='Install a version of Composer without switching to it.'
        )
        install_parser.add_argument(
            'version',
            nargs=1,
            help='Composer version to install.'
        )
