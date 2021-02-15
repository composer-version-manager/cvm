from abc import ABC, abstractmethod


class Shell(ABC):

    @staticmethod
    @abstractmethod
    def get_hook() -> str:
        pass
