from colorama import Fore
from colorama.ansi import AnsiFore


def colored_fore(color: AnsiFore, text: str, default: str = Fore.LIGHTWHITE_EX) -> str:
    return color + text + default

def warning(text: str, default: str = Fore.LIGHTWHITE_EX) -> str:
    return colored_fore(Fore.LIGHTRED_EX, f"cvm: {text}")

def info(text: str, default: str = Fore.LIGHTWHITE_EX) -> str:
    return colored_fore(Fore.LIGHTYELLOW_EX, f"cvm: {text}")
