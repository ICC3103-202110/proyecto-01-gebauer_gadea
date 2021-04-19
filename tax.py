#esta es la clase  de la ccion impuesto
#esta es la clase  de la ccion impuesto

class Tax:
    #CONSTRUCTOR
    def __init__(self,player,i):
        self.player = player
        self.i = i
        
    #METODOS

    def a_tax(self):
        self.player[self.i]._Players__coins += 3
        return 0