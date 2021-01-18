from argparse import Action, Namespace

from src.app.commands.command import Command


class ScanCommand(Command):
    NAME = 'scan'
    DESCRIPTION = 'If present use .cvm_config from the current or specified directory.'

    def exec(self, args: Namespace):
        print("Scan command executed.")
        print(args)

    @staticmethod
    def define_signature(parser: Action):
        parser.add_parser(ScanCommand.NAME, help=ScanCommand.DESCRIPTION)
