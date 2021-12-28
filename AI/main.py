from user_input import Shell
from problems import problems


def main():
    problem = Shell.select_from_list(problems, title="Choose problem:")
    problem.problem_class.main()


if __name__ == "__main__":
    main()
