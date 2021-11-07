from abc import abstractclassmethod


class IService:
    def __init__(self) -> None:
        pass
    @abstractclassmethod
    def ExecuteScoped(self) -> None:
        pass
    @abstractclassmethod
    def CallBack(self,method) -> None:
        pass