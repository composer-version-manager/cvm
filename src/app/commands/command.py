from abc import ABC, abstractmethod, abstractstaticmethod
from argparse import Action


class Command(ABC):
    @abstractmethod
    def handle(self) -> None:
        pass

    @staticmethod
    @abstractmethod
    def define_signature(parser: Action):
        pass
