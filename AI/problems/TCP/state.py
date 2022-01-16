from typing import Set
from interfaces import IState
from .action import TCPAction
from .node import Node


class TCPState(IState):
    def __init__(self, head: Node, visited_nodes: Set[Node], unvisited_nodes: Set[Node], cost: int) -> None:
        self.visited_nodes = visited_nodes
        if not isinstance(visited_nodes, set):
            self.visited_nodes = set(visited_nodes)
        self.unvisited_nodes = unvisited_nodes
        if not isinstance(unvisited_nodes, set):
            self.unvisited_nodes = set(unvisited_nodes)
        self.head = head
        self.cost = cost

    def play(self, action: TCPAction) -> IState:
        head = action.edge.end_node
        next_visited_nodes = self.visited_nodes.copy()
        next_visited_nodes.add(head)
        next_unvisited_nodes = self.unvisited_nodes.copy()
        next_unvisited_nodes.remove(head)
        return TCPState(head, next_visited_nodes, next_unvisited_nodes, self.cost + action.get_cost())

    def get_cost(self) -> int:
        return self.cost

    def __hash__(self) -> int:
        return hash((frozenset(self.visited_nodes), self.head))

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TCPState) and self.head == __o.head and self.visited_nodes == __o.visited_nodes

    def __str__(self) -> str:
        return f"[TCPState](head: {self.head}, visited_nodes: {self.visited_nodes}, unvisited_nodes: {self.unvisited_nodes}, cost: {self.cost})"
