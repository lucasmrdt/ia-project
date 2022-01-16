from user_input import Shell
from problems import problems


def main():
    problem = Shell.select_from_list(problems, title="Choose problem:")
    answer = Shell.select_from_list(
        ["run stats", "run instance"], title="What do you want to do?")
    if answer == "run stats":
        problem.problem_class.stats()
    else:
        problem.problem_class.main()


if __name__ == "__main__":
    main()
