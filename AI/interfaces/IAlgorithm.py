from typing import List

from .IInstance import IInstance
from .ISolution import ISolution


class IAlgorithm:
    def __init__(self, instance: IInstance):
        raise NotImplementedError

    def get_best_solution(self) -> ISolution:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()
