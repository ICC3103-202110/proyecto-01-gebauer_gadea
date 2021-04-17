import random

class General_actions:
    def __init__(self,player,i):
        self.__player = player #lista de jugadores
        self.__i = i   #Jugador que está jugando
            
    @property
    def player(self):
        return self.__player


    @property
    def i(self):
        return self.__i



    def entry(self):
        self.player[self.__i]._Players__coins += 1
        return 0

    def abroad_help(self):
        self.player[self.__i]._Players__coins+= 2  #Falta decir que puede ser bloqueada por el Duque pero lo hacemos dsp
        return 0


    def hit(self):
        against = int(input("Elija un jugador al que quiera realizar esta acción"))
        if against ==  self.__i+1:
            print("No puede hacérselo a usted mismo")
            self.hit()
        elif against <1 or against > len(self.player):
            print("No existe ese jugador")
            self.hit()
        elif self.player[against-1]._Players__seen_cards1 != 0 and (self.player[against-1]._Players__seen_cards2 != 0):
                print("Ese jugador ya tiene sus cartas dadas vuelta")
                self.hit()
        else:
            self.player[self.__i]._Players__coins -=7
            print("Jugador", (against))
            if self.player[against-1]._Players__seen_cards1 != 0:
                print("Sólo le queda una carta, se dará vuelta esa")
                card = 2
            elif self.player[against-1]._Players__seen_cards2 != 0:
                print("Sólo le queda una carta, se dará vuelta esa")
                card = 1
            else:
                card = int(input("Diga la carta que quiera dar vuelta(1 o 2)"))
            self.seen_cards(against,card)


 
    def seen_cards(self,against,card):
        if card != 1 and card != 2:
            print("Esa carta no existe. Se elijirá al azar")
            card = random.randint(1,2)
        if card == 1:
            if self.player[against-1]._Players__seen_cards1 == 0:
                self.player[against-1]._Players__seen_cards1 = self.player[against-1]._Players__influence1
            else:
                self.player[against-1]._Players__seen_cards2 = self.player[against-1]._Players__influence1
        else:
            if self.player[against-1]._Players__seen_cards1 == 0:
                self.player[against-1]._Players__seen_cards1 = self.player[against-1]._Players__influence2
            else: 
                self.player[against-1]._Players__seen_cards2 =self.player[against-1]._Players__influence2


