#esta es la clase de la accion golpe
import random
class Hit:

    #CONSTRUCTOR
    def __init__(self,player,i):
        self.player = player
        self.i = i

        self.type_action()
        
    #METODOS

    def type_action(self):
        return 3 

    def hit(self):
        against = int(input("Elija un jugador al que quiera realizar esta acción"))
        if against ==  self.i+1:
            print("No puede hacérselo a usted mismo")
            self.hit()
        elif against <1 or against > len(self.player):
            print("No existe ese jugador")
            self.hit()
        else: 
            self.player[self.i]._Players__coins -=7  
            self.show_card(against)

 
    def show_card(self,against):
        if self.player[against-1]._Players__seen_cards1 != str([]) and (self.player[against-1]._Players__seen_cards2 != str([])):
            print("Ese jugador ya tiene sus cartas dadas vuelta. Ya perdió. Elija otro")
            self.hit()
        else:
            print("Jugador", (against))
            if self.player[against-1]._Players__seen_cards1 != str([]):
                print("Sólo le queda una carta, se dará vuelta esa")
                print("JUGADOR " +str(against)+ " PIERDE EL JUEGO")
                card = 2  
            elif self.player[against-1]._Players__seen_cards2 != str([]):
                print("Sólo le queda una carta, se dará vuelta esa")
                print("JUGADOR " +str(against)+ " PIERDE EL JUEGO")
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