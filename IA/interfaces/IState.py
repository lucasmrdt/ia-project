from .IAction import IAction


class IState():
    # @dev maybe mutate the state to optimize memory usage
    def play(self, action: IAction) -> IState:
        raise NotImplementedError

    def get_cost(self) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()
