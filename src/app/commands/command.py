from abc import ABC, abstractmethod
from argparse import Action


class Command(ABC):
    @abstractmethod
    def exec(self) -> None:
        pass

    @staticmethod
    @abstractmethod
    def define_signature(parser: Action):
        pass
