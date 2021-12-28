from interfaces import IHeuristic
from .state import TCPState
from .instance import TCPInstance


class TCPHeuristic(IHeuristic):
    def get_h(self, state: TCPState, instance: TCPInstance) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        return "[TCPHeuristic]"
