class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"[Node]({self.name})"


if __name__ == "__main__":
    node1 = Node("node1")
    node2 = Node("node2")
    print(repr(node1))
    print(node2)
