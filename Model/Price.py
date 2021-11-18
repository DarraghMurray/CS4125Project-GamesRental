from abc import ABC, abstractmethod
from enum import Enum

class Prices(Enum):
    Indie = 4.99
    Standard = 9.99
    TripleA = 14.99

class Price(ABC):

    @abstractmethod
    def GetPrice(self):
        pass