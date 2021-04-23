#esta es la clase  de la accion impuesto
from actions import Actions
class Tax(Actions):
    #CONSTRUCTOR
    def __init__(self,player,i):
        super(Tax, self).__init__(player,i)
        
    #METODOS
    def change_coins(self):
        self.player[self.i].coins += 3

    def a_tax(self):
        self.change_coins()
        return 0