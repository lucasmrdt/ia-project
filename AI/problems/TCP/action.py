from interfaces import IAction
from .edge import Edge


class TCPAction(IAction):
    def __init__(self, edge: Edge) -> None:
        self.edge = edge

    def get_cost(self) -> int:
        return self.edge.weight

    def __str__(self) -> str:
        return str(self.edge)

    def __hash__(self) -> int:
        return hash(self.edge)

    def __eq__(self, other) -> bool:
        if not isinstance(other, TCPAction):
            return False
        return self.edge == other.edge
