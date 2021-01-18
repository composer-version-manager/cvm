from argparse import Action

from src.app.commands.command import Command


class UseCommand(Command):
    def handle(self):
        print("Init command handled.")

    @staticmethod
    def define_signature(parser: Action):
        install_parser = parser.add_parser(
            'install',
            help='Install a version of Composer without switching to it.'
        )
        install_parser.add_argument(
            'version',
            nargs=1,
            help='Composer version to install.'
        )
