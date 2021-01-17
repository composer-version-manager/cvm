import sys

MIN_PYTHON = (3, 0)

if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

from colorama import Fore
from app.commands.command import Command


def main():
    print(Fore.LIGHTBLUE_EX + 'Process completed.')
    command = Command()


if __name__ == '__main__':
    main()
