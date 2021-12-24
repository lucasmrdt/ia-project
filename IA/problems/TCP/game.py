from interfaces import IGame, IAlgorithm
from .instance import TCPInstance


class TCPGame(IGame):
    def __init__(self, instance: TCPInstance, algorithm: IAlgorithm) -> None:
        self.instance = instance
        self.algorithm = algorithm

    def run(self) -> None:
        sol = self.algorithm.get_best_solution()
        state = self.instance.get_init_state()
        self.instance.display_state(state)
        for action in sol:
            state = state.play(action)
            self.instance.display_state(state)
