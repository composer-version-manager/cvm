import logging
import sys
from typing import Optional

from cvm.shells.shell import Shell
from cvm.shells.shell_bash import ShellBash
from cvm.shells.shell_zsh import ShellZsh

SHELLS = {
    ShellZsh.NAME: ShellZsh,
    ShellBash.NAME: ShellBash
}


class ShellService:
    @staticmethod
    def get_shell_by_name(name: str) -> Optional[Shell]:
        shell = SHELLS.get(name, None)
        if shell is None:
            logging.error("Shell {} not found".format(name))
            sys.exit(1)

        return shell()
