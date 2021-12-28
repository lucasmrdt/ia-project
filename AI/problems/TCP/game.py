from interfaces import IGame, IAlgorithm
from .instance import TCPInstance


class TCPGame(IGame):
    def __init__(self, instance: TCPInstance, algorithm: IAlgorithm) -> None:
        self.instance = instance
        self.algorithm = algorithm

    def run(self) -> None:
        sol = self.algorithm.get_best_solution()
        state = self.instance.get_init_state()
        print("Do you want to see the solution? (y/n)")
        if input().lower() == "y":
            print(f"\tInitial state:", state)
            for action, state in sol.iter_solve():
                print(f"\t{action} -> {state}")
