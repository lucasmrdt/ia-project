from .IInstance import IInstance
from .ISolution import ISolution


class IAdvisor:
    def __init__(self, instance: IInstance):
        raise NotImplementedError()

    def get_better_solutions(self, sol: ISolution) -> ISolution:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()
