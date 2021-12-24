from typing import List

from .IInstance import IInstance
from .IAction import IAction


class IAlgorithm:
    def __init__(self, instance: IInstance):
        raise NotImplementedError

    def get_best_solution(self) -> List[IAction]:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()
