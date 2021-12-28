from typing import List
from shared import DefaultSolution
from interfaces import IAlgorithm, IInstance, IAction, IHeuristic, IState, ISolution


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
        if self.instance.is_terminal_state(state):
            return []
        for action in self.instance.get_possible_actions(state):
            next_state = state.play(action)
            res = self._solve(next_state)
            if res is not None:
                return [action] + res
        return None
