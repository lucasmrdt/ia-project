from typing import List
from shared import DefaultSolution
from interfaces import IAlgorithm, IInstance, IAction, IHeuristic, IState, ISolution
from heuristic_mst import HeuristiqueMST
import math

class InformedResearchAlgorithm(IAlgorithm):
    def __init__(self, instance: IInstance, heuristic: IHeuristic) -> None:
        self.instance = instance
        self.heuristic = heuristic

    def get_best_solution(self) -> ISolution:
        init_state = self.instance.get_init_state()
        actions = self._solve(init_state)
        return DefaultSolution(init_state, actions)

    def __str__(self) -> str:
        return "InformedResearchAlgorithm"

    # DFS (pas A*)
    def _solve(self, state: IState) -> List[IAction]:
        next_action = None
        if self.instance.is_terminal_state(state):
            return []
        for action in self.instance.get_possible_actions(state):
            if _f(action) < _f(next_action) or next_action is None:
                next_state = action
            next_state = state.play(next_action)
            res = self._solve(next_state)
            if res is not None:
                return [action] + res
        return None

    def _f(self, state: IState) -> int:
        return _g(state) + get_h(state, self.instance)
        
    def _g(self, state: IState) -> int:
        start_node = self.instance.get_init_state()
        end_node = state.head

        current_node = start_node
        g_val = math.inf
        while current_node != end_node:
            for node in self.instance.adj_mat[current_node]:
                for node_ajd in node:
                    if self.instance.adj_mat[current_node][node_ajd] + self.heuristic.get_h(node_ajd) < g_val:
                        g_val+=self.instance.adj_mat[current_node][node_ajd] + self.heuristic.get_h(node_ajd)
                        current_node = node_ajd

