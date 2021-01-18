import argparse
from typing import Optional

from argparse_color_formatter import ColorRawTextHelpFormatter
from colorama import Fore

from src.app.commands.command import Command
from src.app.commands.install_command import InstallCommand
from src.app.commands.scan_command import ScanCommand
from src.app.commands.use_command import UseCommand
from src.app.helpers.helpers import colored_fore

COMMAND_NAME = 'cvm'
COMMAND_DESC = 'Composer Version Manager'
COMMAND_EPILOG = 'https://github.com/game-of-morgan/cvm\n\nSupport this project by giving it a GitHub star ⭐️'

COMMANDS = {
    UseCommand.NAME: UseCommand,
    InstallCommand.NAME: InstallCommand,
    ScanCommand.NAME: ScanCommand
}


def get_command_by_name(name: str) -> Optional[Command]:
    return COMMANDS.get(name, None)()


def run():
    parser = argparse.ArgumentParser(
        colored_fore(Fore.LIGHTGREEN_EX, COMMAND_NAME),
        formatter_class=ColorRawTextHelpFormatter,
        description=colored_fore(Fore.LIGHTYELLOW_EX, COMMAND_DESC),
        epilog=colored_fore(Fore.YELLOW, COMMAND_EPILOG)
    )

    subparsers = parser.add_subparsers(dest='command')
    for command in COMMANDS.values():
        command.define_signature(subparsers)

    args = parser.parse_args()

    command = get_command_by_name(args.command)
    command.exec()
