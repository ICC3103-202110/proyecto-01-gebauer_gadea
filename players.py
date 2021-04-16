class Players:
    def __init__(self,player_number,influence1,influence2,coins):
        self.__player_number = player_number
        self.__influence1 = influence1
        self.__influence2 = influence2
        self.__coins = coins
    @property
    def player_number (self):
        return self.__player_number
    @property
    def influence1 (self):
        return self.__influence1
    @property
    def influence2 (self):
        return self.__influence2
    @property
    def coins (self):
        return self.__coins
    @coins.setter
    def coins(self, value):
        if self.__coins >= 0:
            self.__coins = value
        else: 
            raise ValueError("No tiene suficientes monedas")