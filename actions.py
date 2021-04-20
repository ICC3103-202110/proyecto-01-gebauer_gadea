from abc import ABC, abstractmethod
from change_coins import Change_coins

class Actions(Change_coins,ABC):
    def __init__(self, player, i):
        self.player = player
        self.i = i

    @abstractmethod
    def change_coins(self): 
        pass