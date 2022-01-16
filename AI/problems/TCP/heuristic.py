from shared import MinPriorityQueue
from interfaces import IHeuristic
from .state import TCPState
from .instance import TCPInstance


class TCPHeuristic(IHeuristic):
    def __init__(self, instance: TCPInstance) -> None:
        self.instance = instance

    def get_h(self, state: TCPState) -> int:
        queue = MinPriorityQueue()
        unvisited_nodes = state.unvisited_nodes.copy()
        if state.head in unvisited_nodes:
            unvisited_nodes.remove(state.head)

        for unvis_node in unvisited_nodes:
            weight = self.instance.adj_mat[state.head][unvis_node]
            queue.push((state.head, unvis_node), weight)

        h_val = 0
        while len(unvisited_nodes) > 0:
            start_node, end_node = queue.pop()
            while end_node not in unvisited_nodes:
                start_node, end_node = queue.pop()
            h_val += self.instance.adj_mat[start_node][end_node]
            unvisited_nodes.remove(end_node)
            for unvis_node in unvisited_nodes:
                weight = self.instance.adj_mat[end_node][unvis_node]
                queue.push((end_node, unvis_node), weight)
        return h_val

    def __str__(self) -> str:
        return "[TCPHeuristic]"
