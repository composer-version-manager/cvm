import argparse
import logging
import sys
from typing import Optional

from argparse_color_formatter import ColorRawTextHelpFormatter
from colorama import Fore

from cvm.commands.cache_command import CacheCommand
from cvm.commands.command import Command
from cvm.commands.hook_command import HookCommand
from cvm.commands.list_command import ListCommand
from cvm.commands.scan_command import ScanCommand
from cvm.commands.use_command import UseCommand
from cvm.helpers.cli import colored_fore
from cvm.services.cache_service import CacheService

COMMAND_NAME = 'cvm'
COMMAND_DESC = 'Composer Version Manager\n' + colored_fore(Fore.WHITE, 'Authors: @game-of-morgan (Morgan Wowk), @ubaniak (Bhavek Budhia)')
COMMAND_EPILOG = 'https://github.com/game-of-morgan/cvm\n\nSupport this project by giving it a GitHub star ⭐️'

COMMANDS = {
    UseCommand.NAME: UseCommand,
    ScanCommand.NAME: ScanCommand,
    ListCommand.NAME: ListCommand,
    HookCommand.NAME: HookCommand,
    CacheCommand.NAME: CacheCommand
}


def get_command_by_name(name: str) -> Optional[Command]:
    command = COMMANDS.get(name, None)

    return command


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
    if command is None:
        parser.print_help(sys.stdout)
        return

    command().exec(args)

if __name__ == '__main__':
    main()
