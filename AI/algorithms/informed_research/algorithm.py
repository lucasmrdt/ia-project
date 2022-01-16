from typing import List

from shared import DefaultSolution, MinPriorityQueue
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

    def _f(self, state: IState) -> int:
        return state.get_cost() + self.heuristic.get_h(state)

    def _solve(self, init_state: IState) -> List[IAction]:
        frontier = MinPriorityQueue()
        frontier.push((init_state, []), self._f(init_state))
        visited = set()
        while True:
            head, actions = frontier.pop()
            visited.add(head)
            if self.instance.is_terminal_state(head):
                return actions
            for action in self.instance.get_possible_actions(head):
                state = head.play(action)
                if state not in visited:
                    frontier.push((state, actions + [action]), self._f(state))
