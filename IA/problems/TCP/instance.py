from typing import List
from interfaces import IInstance
from .state import TCPState
from .action import TCPAction


class TCPInstance(IInstance):
    def __init__(self, file_name: str) -> None:
        self.start_node = None
        self.nodes = []

    def get_init_state(self) -> TCPState:
        unvisited_nodes = self.nodes.copy()
        unvisited_nodes.remove(self.start_node)
        return TCPState([self.start_node], unvisited_nodes, 0)

    def get_possible_actions(self, state: TCPState) -> List[TCPAction]:
        return [TCPAction(edge) for edge in state.unvisited_nodes]

    def is_terminal_state(self, state: TCPState) -> bool:
        return len(state.unvisited_nodes) == 0

    def __str__(self) -> str:
        raise NotImplementedError
