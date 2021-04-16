class Players:
    def __init__(self,player_number,influence1,influence2,coins):
        self.player_number = player_number
        self.influence1 = influence1
        self.influence2 = influence2
        self.coins=coins
@property
def player_number(self):
    return self.__player_number
@player_number.setter
def player_number(self, value):
    self.__player_number = value

@property
def influence1(self):
    return self.influence1
@influence1.setter
def influence1(self, value):
    self.influence2 = value

@property
def influence2(self):
    return self.influence2
@influence2.setter
def influence2(self, value):
    self.influence2 = value

@property
def coins(self):
    return self.coins
@coins.setter
def coins(self, value):
    self.coins = value
