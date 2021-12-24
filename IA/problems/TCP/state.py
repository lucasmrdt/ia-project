from typing import List
from interfaces import IState
from .action import TCPAction
from .node import Node


class TCPState(IState):
    def __init__(self, visited_nodes: List[Node], unvisited_nodes: List[Node], cost: int) -> None:
        self.visited_nodes = visited_nodes
        self.unvisited_nodes = unvisited_nodes
        self.cost = cost

    def play(self, action: TCPAction) -> IState:
        self.visited_nodes.append(action.edge.node2)
        self.unvisited_nodes.remove(action.edge.node2)
        self.cost += action.get_cost()

    def get_cost(self) -> int:
        return self.cost

    def __str__(self) -> str:
        raise NotImplementedError
