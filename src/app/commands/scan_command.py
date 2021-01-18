from argparse import Action, Namespace

from src.app.commands.command import Command


class ScanCommand(Command):
    NAME = 'scan'
    DESCRIPTION = 'Use .cvm_config from the current directory if present.'

    def exec(self, args: Namespace):
        print("Scan command executed.")
        print(args)

    @staticmethod
    def define_signature(parser: Action):
        parser.add_parser(ScanCommand.NAME, help=ScanCommand.DESCRIPTION)
