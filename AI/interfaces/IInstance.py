from typing import List
from .IAction import IAction
from .IState import IState


class IInstance():
    def __init__(self) -> None:
        raise NotImplementedError

    def get_init_state(self) -> IState:
        raise NotImplementedError

    def get_possible_actions(self, state: IState) -> List[IAction]:
        raise NotImplementedError

    def is_terminal_state(self, state: IState) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()
