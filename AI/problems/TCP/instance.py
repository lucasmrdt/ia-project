import networkx as nx
import tsplib95
import numpy as np
import matplotlib.pyplot as plt

from typing import List
from interfaces import IInstance
from .edge import Edge
from .node import Node
from .state import TCPState
from .action import TCPAction


class TCPInstance(IInstance):
    def __init__(self, file_name: str) -> None:
        if file_name.endswith(".atsp"):
            problem = tsplib95.load(file_name)
            G: nx.Graph = nx.from_numpy_matrix(
                np.array(problem.edge_weights), create_using=nx.MultiGraph)
            self.G = G
        else:
            raise ValueError("File must be .atsp")
        self.nodes = list(G.nodes)
        self.adj_list = {node: [(Edge(node, n, G.get_edge_data(node, n)[0]['weight']))
                                for n in G.neighbors(node)] for node in G.nodes}
        self.start_node = self.nodes[0]

    def get_init_state(self) -> TCPState:
        unvisited_nodes = self.nodes.copy()
        return TCPState(self.start_node, [], unvisited_nodes, 0)

    def get_possible_actions(self, state: TCPState) -> List[TCPAction]:
        available_neighbors = [
            edge for edge in self.adj_list[state.head] if edge.end_node in state.unvisited_nodes]
        return [TCPAction(edge) for edge in available_neighbors]

    def is_terminal_state(self, state: TCPState) -> bool:
        return len(state.unvisited_nodes) == 0 and state.head == self.start_node

    def display(self) -> None:
        nx.draw(self.G, with_labels=True)
        plt.show()

    def __str__(self) -> str:
        return f"TCPInstance({self.G})"
