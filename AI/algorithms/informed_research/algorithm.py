from typing import List
from interfaces import IAlgorithm, IInstance, IAction, IHeuristic, IState


class InformedResearchAlgorithm(IAlgorithm):
    def __init__(self, instance: IInstance, heuristic: IHeuristic) -> None:
        self.instance = instance
        self.heuristic = heuristic

    def get_best_solution(self) -> List[IAction]:
        init_state = self.instance.get_init_state()
        return self._solve(init_state)

    def __str__(self) -> str:
        raise NotImplementedError

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
