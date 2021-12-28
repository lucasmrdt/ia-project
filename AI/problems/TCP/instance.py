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
        elif file_name.endswith(".txt"):
            with open(file_name) as f:
                lines = f.readlines()
            adj_matrix = [[int(x) for x in line.strip().split()]
                          for line in lines]
            G: nx.Graph = nx.from_numpy_matrix(
                np.array(adj_matrix), create_using=nx.MultiGraph)
            self.G = G
        else:
            raise ValueError("File must be .atsp")
        self.nodes = list(G.nodes)
        self.adj_list = {node: [(Edge(node, n, G.get_edge_data(node, n)[0]['weight']))
                                for n in G.neighbors(node) if n != node] for node in G.nodes}
        self.adj_mat = {a: {b.end_node: b.weight for b in n}
                        for a, n in self.adj_list.items()}
        self.start_node = self.nodes[0]

    def get_init_state(self) -> TCPState:
        unvisited_nodes = self.nodes.copy()
        return TCPState(self.start_node, [], unvisited_nodes, 0)

    def get_possible_actions(self, state: TCPState) -> List[TCPAction]:
        if len(state.unvisited_nodes) == 1 and self.start_node in state.unvisited_nodes:
            final_action = TCPAction(
                Edge(state.head, self.start_node, self.adj_mat[state.head][self.start_node]))
            return [final_action]
        available_neighbors = [
            edge for edge in self.adj_list[state.head]
            if edge.end_node in state.unvisited_nodes
            and edge.end_node != state.head
            and edge.end_node != self.start_node]
        return [TCPAction(edge) for edge in available_neighbors]

    def is_terminal_state(self, state: TCPState) -> bool:
        return len(state.unvisited_nodes) == 0 and state.head == self.start_node

    def display(self) -> None:
        nx.draw(self.G, with_labels=True)
        plt.show()

    def __str__(self) -> str:
        return f"TCPInstance({self.G})"
