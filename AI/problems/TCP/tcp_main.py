import os
from user_input import Shell

from .game import TCPGame
from .instance import TCPInstance
from .heuristic import TCPHeuristic
from algorithms import InformedResearchAlgorithm

base_dir = os.path.join(os.path.dirname(__file__), "instances")


def main():
    instance = Shell.select_from_list(
        os.listdir(base_dir), title="Choose instance:")
    instance = os.path.join(base_dir, instance)
    instance = TCPInstance(instance)
    heuristic = TCPHeuristic()
    algo = InformedResearchAlgorithm(instance, heuristic)
    game = TCPGame(instance, algo)
    game.run()


if __name__ == "__main__":
    main()
