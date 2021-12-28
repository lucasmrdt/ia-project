from interfaces import IAction
from .edge import Edge


class TCPAction(IAction):
    def __init__(self, edge: Edge) -> None:
        self.edge = edge

    def get_cost(self) -> int:
        return self.edge.weight

    def __str__(self) -> str:
        return str(self.edge)
