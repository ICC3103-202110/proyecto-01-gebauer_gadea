
class General_accions:
    def __init__(self,players,i):
        self.__players=players
        self.__i = i
    @property
    def players(self):
        return self.__players
    @property
    def i(self):
        return self.__i

    def entry(self):
        self.__players[self.__i].coins += 1
    def abroad_help(self):
        self.__players[self.__i].coins += 2
    def hit(self):
        self.__players[self.__i].coins -= 7
