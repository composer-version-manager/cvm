from colorama import Fore
from colorama.ansi import AnsiFore


def colored_fore(color: AnsiFore, text: str, default: str = Fore.LIGHTWHITE_EX) -> str:
    return color + text + default
