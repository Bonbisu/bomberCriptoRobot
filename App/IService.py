from abc import abstractclassmethod


class IService:
    def __init__(self) -> None:
        pass
    @abstractclassmethod
    def CallBack() -> None:
        pass