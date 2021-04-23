from actions import Actions

class Extortion(Actions):
    #CONSTRUCTOR
    def __init__(self,player,i):
        super(Extortion, self).__init__(player, i)
        
    #METODOS
    def change_coins(self,n,who):
        self.player[who].coins += n

    def extortion(self):
        print("EL JUGADOR "+str(self.i +1)+" ELIGIÓ LA ACCIÓN EXTORSIÓN")
        print("Elija al jugador que quiere realizar esa acción")
        against = int(input())
        if against ==  self.i+1:
            print("No puede hacérselo a usted mismo")
            self.extortion()
        elif against <1 or against > len(self.player):
            print("No existe ese jugador")
            self.extortion()
        else:
            print("El jugador "+str(self.i +1)+" quiere le quiere quitar monedas al jugador "+str(against))
        self.a_extortion(against)

        
    def a_extortion(self,against):
        if self.player[against-1]._Players__coins == 1:
            self.change_coins(-1,against-1)
            self.change_coins(1,self.i)
            print("Sólo se le quitó una moneda")
        elif self.player[against-1]._Players__coins == 0:
            print("No se le pueden quitar más monedas, pasa a siguiente turno")
        else:
            print("Cuántas monedas quiere quitarle? (0,1,2)")
            answer = int(input())
            if answer != 0 and answer != 1 and answer != 2:
                print("No se puede esa cantidad")
                self.a_extortion(against)
            else:
                self.change_coins(-answer,against-1)
                self.change_coins(answer,self.i)