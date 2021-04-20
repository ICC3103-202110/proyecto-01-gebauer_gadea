class Abroad_help:
    #CONSTRUCTOR
    def __init__(self,player,i):
        self.player = player
        self.i = i

        self.type_action()
        
    #METODOS

    def type_action(self):
        return 2

    def a_abroad_help(self):
        self.player[self.i]._Players__coins += 2
        return 0