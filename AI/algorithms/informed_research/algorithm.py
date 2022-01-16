from typing import List
from shared import DefaultSolution
from interfaces import IAlgorithm, IInstance, IAction, IHeuristic, IState, ISolution
from .heuristicMST import heuristiqueMST
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

    def _f(self, state: IState) -> int:
        return self._g(state) + get_h(state)
        
    def _g(self, state: IState) -> int:

        start_node = self.instance.get_init_state()
        end_node = state.head

        path_val = math.inf
        current_node = start_node
        while current_node != end_node:
            edge_min_val = math.inf
            for actions in self.instance.get_possible_actions(current_node):
                if actions.get_cost() < edge_min_val:
                    edge_min_val = actions.get_cost()
                    current_node = current_node.play(actions)
            path_val+=edge_min_val

    def get_h(self, state: IState) -> int:
        visited_nodes = state.visited_nodes
        unvisited_nodes = state.unvisited_nodes
        
        h_val = 0

        for vis_node in visited_nodes:
            min_weigh = math.inf
            new_vis_node = None
            for unvis_node in unvisited_nodes:
                if vis_node in self.instance.adj_mat and unvis_node in self.instance.adj_mat[vis_node]:
                    if self.instance.adj_mat[vis_node][unvis_node] < min_weigh:
                        min_weigh = self.instance.adj_mat[vis_node][unvis_node]
                        new_vis_node = unvis_node
            h+=min_weigh
            visited_nodes.append(unvis_node)
            unvisited_nodes.remove(unvis_node)
        
        return h_val

    # A*
    def _solve(self, state: IState) -> List[IAction]:
        next_action = None
        if self.instance.is_terminal_state(state):
            return []
        for action in self.instance.get_possible_actions(state):
            if self._f(state.play(action)) < self._f(next_action) or next_action is None:
                next_state = action
            next_state = state.play(next_action)
            res = self._solve(next_state)
            if res is not None:
                return [action] + res
        return None

