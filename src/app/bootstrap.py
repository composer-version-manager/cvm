from colorama import Fore

from src.app.commands.init_command import InitCommand


def run():
    print(Fore.LIGHTBLUE_EX + 'Process completed.')
    command = InitCommand()
    command.handle()
