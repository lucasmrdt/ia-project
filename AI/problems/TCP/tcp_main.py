import os
from user_input import Shell
from time import time

from .game import TCPGame
from .instance import TCPInstance
from .heuristic import TCPHeuristic
from .advisor import TCPAdvisor
from algorithms import InformedResearchAlgorithm, LocalResearchAlgorithm

base_dir = os.path.join(os.path.dirname(__file__), "instances")


def main():
    instance = Shell.select_from_list(
        os.listdir(base_dir), title="Choose instance:")
    instance = os.path.join(base_dir, instance)
    instance = TCPInstance(instance)
    heuristic = TCPHeuristic(instance)
    advisor = TCPAdvisor(instance)
    algo = Shell.select_from_list(
        [
            InformedResearchAlgorithm(instance, heuristic),
            LocalResearchAlgorithm(instance, advisor, init_method="glouton"),
            LocalResearchAlgorithm(
                instance, advisor, init_method="random", nb_random_tries=10),
            LocalResearchAlgorithm(
                instance, advisor, init_method="random", nb_random_tries=20),
            LocalResearchAlgorithm(
                instance, advisor, init_method="random", nb_random_tries=50),
            LocalResearchAlgorithm(
                instance, advisor, init_method="random", nb_random_tries=100),
        ], title="Choose algorithm:")
    game = TCPGame(instance, algo)
    begin = time()
    sol = game.run()
    end = time()
    print(f"Execution time: %.2f ms" % (end - begin))
    print("Do you want to see the solution? (y/n)")
    if input().lower() == "y":
        state = instance.get_init_state()
        print(f"\tInitial state:", state)
        for action, state in sol.iter_solve():
            print(f"\t{action} -> {state}")


def stats():
    blacklist = set(["dantzig42.txt", "fri26.txt"])
    for inst in os.listdir(base_dir):
        if inst in blacklist:
            continue
        instance = os.path.join(base_dir, inst)
        instance = TCPInstance(instance)
        heuristic = TCPHeuristic(instance)
        advisor = TCPAdvisor(instance)
        algos = [
            InformedResearchAlgorithm(instance, heuristic),
            LocalResearchAlgorithm(instance, advisor, init_method="glouton"),
            LocalResearchAlgorithm(
                instance, advisor, init_method="random", nb_random_tries=10),
            LocalResearchAlgorithm(
                instance, advisor, init_method="random", nb_random_tries=20),
            LocalResearchAlgorithm(
                instance, advisor, init_method="random", nb_random_tries=50),
            LocalResearchAlgorithm(
                instance, advisor, init_method="random", nb_random_tries=100),
        ]
        for algo in algos:
            print(f"Runing instance: {inst} with algo: {algo} ...")
            game = TCPGame(instance, algo)
            begin = time()
            sol = game.run()
            end = time()
            print("Solution found: %d" % sol.get_cost())
            print("Execution time: %.2f ms" % (end - begin), end="\n\n")
