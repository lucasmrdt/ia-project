class IAction():
    def get_cost(self) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        raise NotImplementedError

    def __eq__(self, __o: object) -> bool:
        raise NotImplementedError
