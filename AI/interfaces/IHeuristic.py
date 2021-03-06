from .IInstance import IInstance
from .IState import IState


class IHeuristic():
    def __init__(self, instance: IInstance):
        raise NotImplementedError()

    def get_h(self, state: IState) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()
