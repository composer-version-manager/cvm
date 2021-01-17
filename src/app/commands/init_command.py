from src.app.commands.command import Command


class InitCommand(Command):
    def handle(self):
        print("Init command handled.")
