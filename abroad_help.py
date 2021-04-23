from actions import Actions
class Abroad_help(Actions):
    #CONSTRUCTOR
    def __init__(self,player,i):
        super(Abroad_help, self).__init__(player,i)

        
    #METODOS

    def change_coins(self):
        self.player[self.i].coins += 2

    def a_abroad_help(self):
        self.change_coins()
        return 0