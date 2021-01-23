from abc import ABC, abstractmethod
from argparse import Action, Namespace


class Command(ABC):
    @abstractmethod
    def exec(self, args: Namespace) -> None:
        pass

    @staticmethod
    @abstractmethod
    def define_signature(parser: Action):
        pass
