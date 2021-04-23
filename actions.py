from abc import ABC, abstractmethod
from change_coins import Change_coins

class Actions(Change_coins,ABC):
    def __init__(self, player, i):
        self.__player = player
        self.__i = i

    @property
    def player(self):
        return self.__player

    @property
    def i(self):
        return self.__i

    @abstractmethod
    def change_coins(self): 
        pass