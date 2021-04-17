import random
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







    def show_card(self,against,accion):  #el against va con +1
        if self.player[against-1]._Players__seen_cards1 != str([]) and (self.player[against-1]._Players__seen_cards2 != str([])):
            print("Ese jugador ya tiene sus cartas dadas vuelta. Ya perdió. Elija otro")
            if accion == 1:
                self.murder()
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

    
    def murder(self):
        action_number = 1
        print("EL JUGADOR"+str(self.__i +1)+"ELIGIÓ LA ACCIÓN ASESINATO")
        against = int(input("Elija un jugador al que quiera realizar esta acción"))
        if against ==  self.__i+1:
            print("No puede hacérselo a usted mismo")
            self.murder()
        elif against <1 or against > len(self.player):
            print("No existe ese jugador")
            self.murder()
        else:
            print("El jugador "+str(self.__i +1)+" quiere asesinar al jugador "+str(against))

        self.block_card(action_number,against)
 


    def block_card(self,action_number,against):
        challenge  = []
        attack = []
        if action_number == 1:
            bloqueo = "Condesa"
            accion = "Asesinato"
            action_card = "A"
            blocking_card = "Co"

        elif accion == 2:
            print("hola")

        for j in range(0, len(self.__player)):
            if j != self.i:
                print("\nJugador "+str(j+1)+", elija una opción.")
                print("\n1. POSEO LA CARTA "+bloqueo +" Y QUIERO CONTRA-ATACAR", accion, " DEL JUGADOR ", str(self.__i+1))
                print("\n2. DESAFIAR A JUGADOR"+str(self.__i+1))
                print("0. NADA\n")
                a = int(input())
                if a == 1:
                    attack.append(j)
                elif a == 2:
                    challenge.append(j)

                elif a !=0 and a != 1:
                    print("Esa opción no es correcta, se asimila que no quiere hacer nada")
                    a = 0
        if len(challenge) >0:   #Tiene prioridad el desafío
            selected_challenge = random.randint(0,len(challenge)-1)  #Se elije un desafio al azar de los que decidieron desafiar
            j = challenge[selected_challenge] #j es jugador que desafía -1
            print("--------------El jugador "+ str(j+1) +" realiza un desafío a jugador "+str(self.__i+1)+"-------------")
            
            if self.player[self.__i]._Players__influence1 != action_card and self.player[self.__i]._Players__influence2 != action_card:
                print("El jugador "+str(self.__i+1)+" no posee la influencia "+action_card+", da vuelta una carta")
                self.show_card(self.__i+1, action_number)      #Como no posee la influencia, la acción no se realiza

            
            elif self.player[self.__i]._Players__influence1 == action_card:
                print("El jugador "+str(self.__i +1)+" posee la influencia "+action_card + ", el jugador "+str(j+1)+" da vuelta una carta")
                self.show_card(j+1,action_number)

                print("El jugador "+str(self.__i +1)+" devuelve su carta al mazo y saca otra")
                self.make_murder(against)         #Como posee la influencia, la acción se realiza al jugador elegido
                return 1, self.__i

            elif self.player[self.__i]._Players__influence2 == action_card:
                print("El jugador "+str(self.__i +1)+" posee la influencia "+action_card + ", el jugador "+str(j+1)+" da vuelta una carta")
                self.show_card(j+1,action_number)
                print("El jugador "+str(self.__i +1)+" devuelve su carta al mazo y saca otra.")
                self.make_murder(self,against)         #Como posee la influencia, la acción se realiza
                return 2, self.__i

    def make_murder(self,against):
        print("Se realiza el asesinato al jugador"+str(against))
