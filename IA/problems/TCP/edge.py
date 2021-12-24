from .node import Node


class Edge:
    def __init__(self, node1: Node, node2: Node, weight: int):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __str__(self):
        return f"{self.node1} -> {self.node2} ({self.weight})"
