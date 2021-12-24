from .IInstance import IInstance


class IGame():
    def __init__(self, instance: IInstance) -> None:
        raise NotImplementedError

    def run(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()
