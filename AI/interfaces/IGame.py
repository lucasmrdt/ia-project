from .IInstance import IInstance
from .ISolution import ISolution


class IGame():
    def __init__(self, instance: IInstance) -> None:
        raise NotImplementedError

    def run(self) -> ISolution:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()
