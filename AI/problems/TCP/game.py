from interfaces import IGame, IAlgorithm
from .instance import TCPInstance


class TCPGame(IGame):
    def __init__(self, instance: TCPInstance, algorithm: IAlgorithm) -> None:
        self.instance = instance
        self.algorithm = algorithm

    def run(self):
        return self.algorithm.get_best_solution()
