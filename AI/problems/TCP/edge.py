from .node import Node


class Edge:
    def __init__(self, start_node: Node, end_node: Node, weight: int):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight

    def __str__(self):
        return f"[Edge]({self.start_node}->{self.end_node} {{{self.weight}}})"

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return hash((self.start_node, self.end_node))

    def __eq__(self, other) -> bool:
        if not isinstance(other, Edge):
            return False
        return self.start_node == other.start_node and self.end_node == other.end_node
