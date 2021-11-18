from abc import ABC, abstractmethod
from enum import Enum

class Prices(Enum):
    OldRelease = .15
    Standard = .2
    NewRelease = .25

class Price(ABC):

    @abstractmethod
    def GetPrice(self, baseRental):
        pass