from typing import Generator, List, Tuple
from .IAction import IAction
from .IState import IState


class ISolution:
    def __init__(self, init_state: IState, actions: List[IAction]):
        raise NotImplementedError()

    def get_cost(self) -> int:
        raise NotImplementedError()

    def get_actions(self) -> List[IAction]:
        raise NotImplementedError()

    def iter_solve(self) -> Generator[Tuple[IAction, IState], None, None]:
        raise NotImplementedError()

    def copy(self):
        raise NotImplementedError()

    def update(self, actions: List[IAction]):
        raise NotImplementedError()

    def __hash__(self) -> int:
        raise NotImplementedError()

    def __eq__(self, __o: object) -> bool:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()

    def __repr__(self) -> str:
        return str(self)
