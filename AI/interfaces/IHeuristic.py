from .IInstance import IInstance
from .IState import IState


class IHeuristic():
    def get_h(self, state: IState, instance: IInstance) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()
