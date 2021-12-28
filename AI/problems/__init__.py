from . import TCP


class Problem:
    def __init__(self, name, problem_class):
        self.name = name
        self.problem_class = problem_class

    def __str__(self) -> str:
        return self.name


problems = [Problem("TCP", TCP)]
