import random

from typing import Callable, List
from interfaces import IAlgorithm, IInstance, IAction, IState, ISolution, IAdvisor
from utils import Analysis
from shared import DefaultSolution


class LocalResearchAlgorithm(IAlgorithm):
    def __init__(self, instance: IInstance, advisor: IAdvisor, init_method="random", algo="hill-climbing", nb_random_tries=1) -> None:
        """Local research algorithm.

        Args:
            instance (IInstance): Problem instance.
            advisor (IAdvisor): Advisor to get better solutions.
            init_method ("random"|"glouton", optional): Method to generate the initial solution. Defaults to "random".
            algo ("hill-climbing", optional): Method to explore solutions. Defaults to "hill-climbing".
            nb_random_tries (int): Number of tries for random resolution.
        """
        assert isinstance(instance, IInstance)
        assert isinstance(advisor, IAdvisor)
        assert init_method in ["random", "glouton"]
        assert algo in ["hill-climbing"]
        assert not nb_random_tries or isinstance(nb_random_tries, int)
        self.instance = instance
        self.advisor = advisor
        self.init_method = init_method
        self.algo = algo
        self.nb_random_tries = nb_random_tries

    def get_best_solution(self) -> ISolution:
        Analysis.reset_all()
        init_state = self.instance.get_init_state()
        sol = None
        nb_iter = self.init_method == "random" and self.nb_random_tries or 1

        print("Solving...")
        for i in range(nb_iter):
            if self.init_method == "random":
                sol_actions = self._create_random_sol(init_state)
            elif self.init_method == "glouton":
                sol_actions = self._create_glouton_sol(init_state)
            else:
                raise Exception(f"Unknown init_method {self.init_method}")
            curr_sol = DefaultSolution(init_state, sol_actions)
            print(f"\t[{i}] initial solution:", curr_sol.get_cost())
            if self.algo == "hill-climbing":
                curr_sol = self._hill_climbing_search(curr_sol)
            else:
                raise Exception(f"Unknown algo {self.algo}")
            if not sol or curr_sol.get_cost() < sol.get_cost():
                sol = curr_sol
                print(f"\t[{i}] New best solution:", sol.get_cost())

        print("Analysis:")
        print("\tTotal iterations:", Analysis.get_all_counts())
        print("\tNb sub-solutions:", Analysis.get_count("sub-solutions"))
        print("\tNb better solutions:", Analysis.get_count("better-solutions"))
        print("Solution:", sol.get_cost())

        return sol

    def __str__(self) -> str:
        return f"LocalResearchAlgorithm({self.init_method}, {self.algo}, nb_random_tries={self.nb_random_tries})"

    def _create_random_sol(self, state: IState) -> List[IAction]:
        def sort_fct(actions: List[IAction]) -> List[IAction]:
            random.shuffle(actions)
            return actions
        return self._create_init_sol(state, sort_fct)

    def _create_glouton_sol(self, state: IState) -> List[IAction]:
        def sort_fct(actions: List[IAction]) -> List[IAction]:
            actions.sort(key=lambda a: a.get_cost())
            return actions
        return self._create_init_sol(state, sort_fct)

    def _create_init_sol(self, state: IState, sort_fct: Callable[[List[IAction]], List[IAction]]) -> List[IAction]:
        if self.instance.is_terminal_state(state):
            return []
        possible_actions = self.instance.get_possible_actions(state)
        possible_actions = sort_fct(possible_actions)
        for action in possible_actions:
            next_state = state.play(action)
            res = self._create_glouton_sol(next_state)
            if res is not None:
                return [action] + res
        return None

    def _hill_climbing_search(self, sol: ISolution) -> ISolution:
        best_sol = sol
        prev_sol = None
        while best_sol != prev_sol:
            prev_sol = best_sol
            better_solutions = self.advisor.get_better_solutions(best_sol)
            for sol in Analysis.count_iterations("better-solutions", better_solutions):
                if sol.get_cost() < best_sol.get_cost():
                    best_sol = sol
        return best_sol

    # @XXX wip
    # def _enhance_sol(self, sol: ISolution) -> ISolution:
    #     best_sol = sol
    #     frontier = [sol]
    #     already_seen = set()
    #     while frontier:
    #         curr_sol = frontier.pop()
    #         better_solutions = Analysis.count_iterations(
    #             "better-solutions", self.advisor.get_better_solutions(curr_sol))
    #         for sol in better_solutions:
    #             if sol in already_seen:
    #                 continue
    #             already_seen.add(sol)
    #             frontier.append(sol)
    #             if sol.get_cost() < best_sol.get_cost():
    #                 best_sol = sol
    #     return best_sol
