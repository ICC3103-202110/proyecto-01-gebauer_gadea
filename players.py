class Players:
    def __init__(self,player_number,influence1,influence2,coins,seen_cards1 = str([]), seen_cards2 = str([])):
        self.__player_number = player_number
        self.__influence1 = influence1
        self.__influence2 = influence2
        self.__coins = coins
        self.__seen_cards1 = seen_cards1
        self.__seen_cards2 = seen_cards2

    @property
    def player_number (self):
        return self.__player_number
    @property
    def seen_cards2 (self):
        return self.__seen_cards2
    @property
    def seen_cards1 (self):
        return self.__seen_cards1
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
        print("Setter de coins")
        if self.__coins >= 0:
            self.__coins = value
        else: 
            raise ValueError("No tiene suficientes monedas")