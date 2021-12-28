from typing import Generator, List, Tuple
from interfaces import IAction, IState, ISolution


class DefaultSolution(ISolution):
    def __init__(self, init_state: IState, actions: List[IAction]):
        self.init_state = init_state
        self.actions = actions
        self.cost = self._compute_cost()

    def get_cost(self) -> int:
        return self.cost

    def get_actions(self) -> List[IAction]:
        return self.actions

    def iter_solve(self) -> Generator[Tuple[IAction, IState], None, None]:
        state = self.init_state
        for action in self.actions:
            state = state.play(action)
            yield action, state

    def update(self, actions) -> None:
        self.actions = actions
        self.cost = self._compute_cost()

    def copy(self) -> ISolution:
        return DefaultSolution(self.init_state, self.actions.copy())

    def __str__(self) -> str:
        return f"DefaultSolution(cost={self.cost}, actions={self.actions})"

    def __hash__(self) -> int:
        return hash(tuple(self.actions))

    def __eq__(self, other) -> bool:
        if not isinstance(other, DefaultSolution):
            return False
        return self.cost == other.cost and self.actions == other.actions

    def _compute_cost(self) -> int:
        state = self.init_state
        cost = 0
        for action in self.actions:
            state = state.play(action)
            cost += action.get_cost()
        return cost
