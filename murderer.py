import random
class Murder:
    #CONSTRUCTOR
    def __init__(self,player,i):
        self.player = player
        self.i = i
        
    #METODOS


    def murder(self):
        print("EL JUGADOR "+str(self.i +1)+" ELIGIÓ LA ACCIÓN ASESINATO")
        against = int(input("Elija un jugador al que quiera realizar esta acción"))
        if against ==  self.i+1:
            print("No puede hacérselo a usted mismo")
            self.murder()
        elif against <1 or against > len(self.player):
            print("No existe ese jugador")
            self.murder()
        else:
            print("El jugador "+str(self.i +1)+" quiere asesinar al jugador "+str(against))
        self.make_murder(against)



    def show_card(self,against):
        
        print("Jugador", (against))
        if self.player[against-1]._Players__seen_cards1 != str([]):
            print("Sólo le queda una carta, se dará vuelta esa")
            print("JUGADOR " +str(against)+ " PIERDE EL JUEGO")
            self.player[against-1]._Players__player_number = 0
            card = 2  
        elif self.player[against-1]._Players__seen_cards2 != str([]):
            print("Sólo le queda una carta, se dará vuelta esa")
            print("JUGADOR " +str(against)+ " PIERDE EL JUEGO")
            self.player[against-1]._Players__player_number = 0
            card = 1
        else:
            card = int(input("Diga la carta que quiera dar vuelta(1 o 2)"))
        if card != 1 and card != 2:
            print("Esa carta no existe. Se elijirá al azar")
            card = random.randint(1,2)
        if card == 1:
                self.player[against-1]._Players__seen_cards1 = "["+str(self.player[against-1]._Players__influence1)+"]"

        else:
                self.player[against-1]._Players__seen_cards2 = "["+str(self.player[against-1]._Players__influence2)+"]"  

    def make_murder(self,against):
        print("Se realiza el asesinato al jugador"+str(against))
        self.show_card(against)