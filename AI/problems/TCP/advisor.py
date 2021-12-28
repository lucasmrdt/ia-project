from typing import List
from itertools import combinations

from interfaces import IAdvisor, ISolution
from .edge import Edge
from .action import TCPAction
from .instance import TCPInstance
from utils import Analysis


class TCPAdvisor(IAdvisor):
    def __init__(self, instance: TCPInstance) -> None:
        self.instance = instance

    def get_better_solutions(self, sol: ISolution) -> ISolution:
        actions: List[TCPAction] = sol.get_actions()
        N = len(actions)
        route = [action.edge.start_node for action in actions]
        extended_route = route + [route[0]]
        adj_mat = self.instance.adj_mat
        jk_combinations = combinations(range(1, N), 2)
        for j, k in Analysis.count_iterations("sub-solutions", jk_combinations):
            i, j, k, l = j - 1, j, k, k + 1
            if i == l:
                continue
            a, b, c, d = extended_route[i], extended_route[j], extended_route[k], extended_route[l]
            prev_cost = adj_mat[a][b] + adj_mat[c][d]
            new_cost = adj_mat[a][c] + adj_mat[b][d]
            if new_cost > prev_cost:
                continue
            new_extended_route = self.two_opt_swap(extended_route, j, k)
            new_route = new_extended_route[:-1]
            yield self.create_new_sol(sol, new_route)

    def two_opt_swap(self, extended_route, j, k):
        return extended_route[:j] + extended_route[j:k+1][::-1] + extended_route[k+1:]

    def create_new_sol(self, prev_sol: ISolution, new_route: List[TCPAction]):
        new_sol = prev_sol.copy()
        new_actions = []
        N = len(new_route)
        for i in range(N):
            start_node = new_route[i]
            end_node = new_route[(i + 1) % N]
            edge = Edge(start_node, end_node,
                        self.instance.adj_mat[start_node][end_node])
            new_actions.append(TCPAction(edge))
        new_sol.update(new_actions)
        return new_sol
