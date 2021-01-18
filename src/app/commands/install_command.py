from argparse import Action

from src.app.commands.command import Command


class InstallCommand(Command):
    def handle(self):
        print("Init command handled.")

    @staticmethod
    def define_signature(parser: Action):
        use_parser = parser.add_parser(
            'use',
            help="Install and use a specific version of Composer."
        )
        use_parser.add_argument(
            'version',
            nargs=1,
            help='Composer version to use.'
        )
