from argparse import Action

from src.app.commands.command import Command


class UseCommand(Command):
    NAME = 'use'
    DESCRIPTION = 'Use a specific version of Composer. Defaulting to the latest-\nstable version when there is a lack of specificity.\n\n'

    def exec(self):
        print("Use command executed.")

    @staticmethod
    def define_signature(parser: Action):
        use_parser = parser.add_parser(UseCommand.NAME, help=UseCommand.DESCRIPTION)
        use_parser.add_argument(
            'version',
            nargs=1,
            help='Composer version to use.',
            metavar='{version}'
        )
