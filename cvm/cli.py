import argparse
import logging
import sys
from typing import Optional

from cvm.helpers.cli import colored_fore
from argparse_color_formatter import ColorRawTextHelpFormatter
from colorama import Fore

from cvm.commands.command import Command
from cvm.commands.use_command import UseCommand
from cvm.commands.install_command import InstallCommand
from cvm.commands.scan_command import ScanCommand
from cvm.commands.list_command import ListCommand

from cvm.services.cache_service import CacheService


COMMAND_NAME = 'cvm'
COMMAND_DESC = 'Composer Version Manager\n' + colored_fore(Fore.WHITE, 'Author: @game-of-morgan (Morgan Wowk)')
COMMAND_EPILOG = 'https://github.com/game-of-morgan/cvm\n\nSupport this project by giving it a GitHub star ⭐️'

COMMANDS = {
    UseCommand.NAME: UseCommand,
    InstallCommand.NAME: InstallCommand,
    ScanCommand.NAME: ScanCommand,
    ListCommand.NAME: ListCommand
}


def get_command_by_name(name: str) -> Optional[Command]:
    command = COMMANDS.get(name, None)
    if command is None:
        logging.error("Command {} not found".format(name))
        sys.exit(1)

    return command()


def main():
    CacheService.boot_cache()
    parser = argparse.ArgumentParser(
        colored_fore(Fore.LIGHTGREEN_EX, COMMAND_NAME),
        formatter_class=ColorRawTextHelpFormatter,
        description=colored_fore(Fore.LIGHTYELLOW_EX, COMMAND_DESC),
        epilog=colored_fore(Fore.YELLOW, COMMAND_EPILOG)
    )
    parser._positionals.title = 'Available commands'
    parser._optionals.title = 'Optional arguments'

    subparsers = parser.add_subparsers(dest='command', metavar='')
    for command in COMMANDS.values():
        command.define_signature(subparsers)

    args = parser.parse_args()

    command = get_command_by_name(args.command)
    command.exec(args)
