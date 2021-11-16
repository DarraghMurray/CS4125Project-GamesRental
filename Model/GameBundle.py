from typing import List
from Model.StoreItem import StoreItem

class GameBundle(StoreItem):

    def __init__(self):
        self._games: List[StoreItem] = []

    def add(self, storeItem: StoreItem) -> None:
        self._games.append(storeItem)
        storeItem.parent = self

    def remove(self, storeItem: StoreItem) -> None:
        self._children.remove(storeItem)
        storeItem.parent = None

    def is_composite(self) -> bool:
        return True

    def getPrice(self) -> float:
        total = 0
        for child in self._games:
            total += child.getPrice()
        return total
