from abc import ABC, abstractmethod

class Price(ABC):
    @abstractmethod
    def GetPrice(self):
        pass