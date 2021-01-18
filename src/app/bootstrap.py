import argparse
from colorama import Fore
from argparse_color_formatter import ColorHelpFormatter

from src.app.commands.install_command import InstallCommand
from src.app.commands.use_command import UseCommand
from src.app.helpers.helpers import colored_fore


def run():
    parser = argparse.ArgumentParser(
        colored_fore(Fore.LIGHTGREEN_EX, 'Composer Version Manager'),
        formatter_class=ColorHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command')

    UseCommand.define_signature(subparsers)
    InstallCommand.define_signature(subparsers)

    args = parser.parse_args()

    print(args)
