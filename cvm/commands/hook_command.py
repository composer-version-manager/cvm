from argparse import Action, Namespace

from cvm.commands.command import Command
from cvm.services.shell_service import ShellService


class HookCommand(Command):
    NAME = 'hook'
    DESCRIPTION = 'Hook cvm to a shell.'

    def exec(self, args: Namespace):
        target = args.shell[0]

        shell_service = ShellService()
        shell = shell_service.get_shell_by_name(target)

        hook = shell.get_hook()

        print(hook)

    @staticmethod
    def define_signature(parser: Action):
        hook_parser = parser.add_parser(HookCommand.NAME, help=HookCommand.DESCRIPTION)
        hook_parser.add_argument(
            'shell',
            nargs=1,
            help='Shell name to hook onto.',
            metavar='{shell}'
        )
