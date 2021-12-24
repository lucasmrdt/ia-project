from interfaces import IAction
from .edge import Edge


class TCPAction(IAction):
    def __init__(self, edge: Edge) -> None:
        self.edge = edge

    def get_cost(self) -> int:
        raise self.edge.weight

    def __str__(self) -> str:
        raise self.edge.__str__()
