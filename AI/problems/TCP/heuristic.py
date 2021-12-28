from interfaces import IHeuristic
from .state import TCPState
from .instance import TCPInstance


class TCPHeuristic(IHeuristic):
    def __init__(self, instance: TCPInstance) -> None:
        self.instance = instance

    def get_h(self, state: TCPState) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        return "[TCPHeuristic]"
