import argparse
from typing import Optional

from argparse_color_formatter import ColorHelpFormatter
from colorama import Fore

from src.app.commands.command import Command
from src.app.commands.install_command import InstallCommand
from src.app.commands.use_command import UseCommand
from src.app.helpers.helpers import colored_fore

COMMANDS = {
    UseCommand.NAME: UseCommand,
    InstallCommand.NAME: InstallCommand
}


def get_command_by_name(name: str) -> Optional[Command]:
    return COMMANDS.get(name, None)()


def run():
    parser = argparse.ArgumentParser(
        colored_fore(Fore.LIGHTGREEN_EX, 'Composer Version Manager'),
        formatter_class=ColorHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command')
    for command in COMMANDS.values():
        command.define_signature(subparsers)

    args = parser.parse_args()

    command = get_command_by_name(args.command)
    command.exec()
