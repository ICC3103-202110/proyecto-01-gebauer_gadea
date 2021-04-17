
class Character_actions:
    def __init__(self,player,influences,i):
        self.__player = player #lista de jugadores
        self.__influences = influences
        self.__i = i   #Jugador que está jugando
            
    @property
    def player(self):
        return self.__player

    @property
    def influences(self):
        return self.__influences

    @property
    def i(self):
        return self.__i

    def tax(self):
        self.player[self.__i]._Players__coins += 3
        return 0
    def murder(self):
        against = int(input("Elija un jugador al que quiera realizar esta acción"))
        if against ==  self.__i+1:
            print("No puede hacérselo a usted mismo")
            self.murder()
        elif against <1 or against > len(self.player):
            print("No existe ese jugador")
            self.murder()
        elif self.player[against-1]._Players__seen_cards1 != 0 and (self.player[against-1]._Players__seen_cards2 != 0):
                print("Ese jugador ya tiene sus cartas dadas vuelta")
                self.murder()
        else:
            self.player[self.__i]._Players__coins -= 3
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

    def extortion(self):
        self.player[self.__i]._Players__coins += 2
        return 0
    def change(self):
        numbers = ['1','2','3','4']
        cards_change=['','','','']
        card1=self.player[self.__i]._Players__influence1
        cards_change[0]=card1
        card2=self.player[self.__i]._Players__influence2
        cards_change[1]=card2
        card3=self.__influences[0]
        self.__influences.pop(0)
        cards_change[2]=card3
        card4=self.__influences[1]
        self.__influences.pop(1)
        cards_change[3]=card4
        
        i=1
        while i!=0:
            print(f" 1:{card1}  2:{card2}  3:{card3}  4:{card4}")
            card_tuple = input("Elija 2 cartas (ej 1,2)")
            if len(card_tuple)>3 or card_tuple[1]!=',':
                print("Cartas mal ingresadas")
            elif card_tuple[0] not in numbers or card_tuple[2] not in numbers:
                print("Cartas mal ingresadas")
            elif int(card_tuple[0])==int(card_tuple[2]):
                print("Cartas mal ingresadas")
            else:
                p1 = int(card_tuple[0])-1
                p2 = int(card_tuple[2])-1
                card1_selected=cards_change[p1]
                card2_selected=cards_change[p2]
                cards_change.pop(p1)
                cards_change.pop(p2-1)
                self.player[self.__i]._Players__influence1 = card1_selected
                self.player[self.__i]._Players__influence2 = card2_selected
                for i in cards_change:
                    self.__influences.append(i)
                print(f"TUS NUEVAS CARTAS SON: {self.player[self.__i]._Players__influence1},{self.player[self.__i]._Players__influence2}") 
                i=0
        return 0
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