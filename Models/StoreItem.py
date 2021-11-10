from abc import ABC, abstractmethod

class StoreItem(ABC):

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, storeItem) -> None:
        pass

    def remove(self, storeItem) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def getPrice(self) -> str:
        pass