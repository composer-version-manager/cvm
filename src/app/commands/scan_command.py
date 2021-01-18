from argparse import Action

from src.app.commands.command import Command


class ScanCommand(Command):
    NAME = 'scan'
    DESCRIPTION = 'Use .cvm_config from the current directory if present.'

    def exec(self):
        print("Scan command executed.")

    @staticmethod
    def define_signature(parser: Action):
        parser.add_parser(ScanCommand.NAME, help=ScanCommand.DESCRIPTION)
