from argparse import Action

from src.app.commands.command import Command


class UseCommand(Command):
    NAME = 'use'

    def exec(self):
        print("Use command executed.")

    @staticmethod
    def define_signature(parser: Action):
        use_parser = parser.add_parser(
            UseCommand.NAME,
            help="Install and use a specific version of Composer."
        )
        use_parser.add_argument(
            'version',
            nargs=1,
            help='Composer version to use.'
        )
