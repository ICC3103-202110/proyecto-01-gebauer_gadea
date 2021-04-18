import random
class Character_actions:

    def __init__(self,player,i):
        self.__player = player #lista de jugadores
        self.__i = i   #Jugador que está jugando
            
    @property
    def player(self):
        return self.__player


    @property
    def i(self):
        return self.__i

    def tax(self):
        self.player[self.__i]._Players__coins += 3
        return 0
        

    def change(self,card1,card2,influences):
        list1 = [card1,card2,self.player[self.__i]._Players__influence1,self.player[self.__i]._Players__influence2]
        print("ACCIÓN CAMBIAR CARTAS")
        print(f" 1:{list1[0]}  2:{list1[2]}  3:{list1[3]}  4:{list1[3]}")
        print("Elije la primera carta para quedarte")
        answer = int(input())
        print("Elije la segunda carta para quedarte")
        answer2 = int(input())
        if answer != 1 and answer != 2 and answer != 3 and answer != 4:
            print("Carta 1 incorrecta. Trate otra vez")
            self.change(card1,card2,influences)
        elif answer2 != 1 and answer2 != 2 and answer2 != 3 and answer2 != 4:
            print("Carta 2 incorrecta. Trate otra vez")
            self.change(card1,card2, influences)
        else:
            self.player[self.__i]._Players__influence1 = list1[answer]
            self.player[self.__i]._Players__influence2 = list1[answer2]
        for i in range(0,4):
            if i != answer and i != answer2:
                influences.append(list1[i])
        return influences




    def show_card(self,against,accion):  #el against va con +1
        if self.player[against-1]._Players__seen_cards1 != str([]) and (self.player[against-1]._Players__seen_cards2 != str([])):
            print("Ese jugador ya tiene sus cartas dadas vuelta. Ya perdió")
            if accion == 1:
                self.murder()
        else:
            print("Jugador", (against))
            if self.player[against-1]._Players__seen_cards1 != str([]):
                print("Sólo le queda una carta, se dará vuelta esa")
                print("JUGADOR " +str(against)+ " PIERDE EL JUEGO")
                self.player.remove(against-1)
                card = 2  
            elif self.player[against-1]._Players__seen_cards2 != str([]):
                print("Sólo le queda una carta, se dará vuelta esa")
                print("JUGADOR " +str(against)+ " PIERDE EL JUEGO")
                self.player.remove(against-1)
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
        print("EL JUGADOR "+str(self.__i +1)+" ELIGIÓ LA ACCIÓN ASESINATO")
        against = int(input("Elija un jugador al que quiera realizar esta acción"))
        if against ==  self.__i+1:
            print("No puede hacérselo a usted mismo")
            self.murder()
        elif against <1 or against > len(self.player):
            print("No existe ese jugador")
            self.murder()
        else:
            print("El jugador "+str(self.__i +1)+" quiere asesinar al jugador "+str(against))
        return against


    def extortion1(self):
        print("EL JUGADOR "+str(self.__i +1)+" ELIGIÓ LA ACCIÓN EXTORSIÓN")
        print("Elija al jugador que quiere realizar esa acción")
        against = int(input())
        if against ==  self.__i+1:
            print("No puede hacérselo a usted mismo")
            self.extortion1()
        elif against <1 or against > len(self.player):
            print("No existe ese jugador")
            self.extortion1()
        else:
            print("El jugador "+str(self.__i +1)+" quiere asesinar al jugador "+str(against))
        return against

        
    def extortion(self,against):
        if self.player[against-1]._Players__coins == 1:
            self.player[against-1]._Players__coins -=1
            print("Sólo se le quitó una moneda")
        else:
            print("Cuántas monedas quiere quitarle? (0,1,2)")
            answer = int(input())
            if answer != 0 and answer != 1 and answer != 2:
                print("No se puede esa cantidad")
                self.extortion(against)
            else:
                self.player[against-1]._Players__coins -= answer
 
    def block_card2(self,action_number):
        attack = []
        challenge = []
        against = self.extortion1()
        bloqueo = "EMBAJADOR"
        bloqueo2 = "CAPITÁN"
        accion =  "EXTORSIÓN"
        action_card = "Ca"
        blocking_card = "E"
        blocking_card2 = "Ca"

        for j in range(0, len(self.__player)):
            if j != self.i:
                print("\nJugador "+str(j+1)+", elija una opción.")
                print("1. POSEO LA CARTA "+bloqueo+" ó "+bloqueo2+" Y QUIERO CONTRA-ATACAR",accion, " DEL JUGADOR ",str(self.__i+1))
                print("2. DESAFIAR A JUGADOR "+str(self.__i+1))
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
                self.show_card(self.__i+1, action_number)      #Como no posee la influencia, la acción no se realiza, no gasta monedas
                return 0, 0
            
            elif self.player[self.__i]._Players__influence1 == action_card:
                print("El jugador "+str(self.__i +1)+" posee la influencia "+action_card + ", el jugador "+str(j+1)+" da vuelta una carta")
                self.show_card(j+1,action_number)
                print("El jugador "+str(self.__i +1)+" devuelve su carta al mazo y saca otra")
                self.extortion(against)        #Como posee la influencia, la acción se realiza al jugador elegido
                return 1, self.__i

            elif self.player[self.__i]._Players__influence2 == action_card:
                print("El jugador "+str(self.__i +1)+" posee la influencia "+action_card + ", el jugador "+str(j+1)+" da vuelta una carta")
                self.show_card(j+1,action_number)
                print("El jugador "+str(self.__i +1)+" devuelve su carta al mazo y saca otra.")
                self.extortion(against)         #Como posee la influencia, la acción se realiza
                return 2, self.__i
        #FALTAN LOS CONRAATAQUES
        if len(attack) > 0:
            selected_attack = random.randint(0,len(attack)-1)
            j = attack[selected_attack]
            print("--------------El jugador "+ str(j+1) +" realiza un contra-ataque a jugador "+str(self.i+1)+"-------------")
            for a in range(0, len(self.__player)):
                if a != j:
                    print("\nJugador "+str(a+1)+", elija una opción.")
                    print("\n1. DESAFIAR A JUGADOR", j+1)
                    print("0. NO HACER NADA")
                    b = int(input())
                    if b == 1:
                        challenge.append(a)
            if len(challenge) >0:           #si alguien quiso desafiar
                selected_challenge = random.randint(0,len(challenge)-1)
                a = challenge[selected_challenge]
                print("--------------El jugador "+str(a+1)+" realiza un desafío a jugador "+str(j+1)+"-------------")
                if self.player[j]._Players__influence1 != blocking_card and self.player[j]._Players__influence2 != blocking_card and self.player[j]._Players__influence1 != blocking_card2 and self.player[j]._Players__influence2 != blocking_card2:
                        print("El jugador "+str(j+1)+" no posee la influencia "+bloqueo+" ni "+ bloqueo2 +", da vuelta una carta")
                        self.show_card(j+1,action_number) #La acción se realiza porque el contraataque fue falso
                        self.extortion(against)
                        return 0, 0
                elif self.player[j]._Players__influence1 == blocking_card:
                        print("El jugador "+str(j+1)+" posee la influencia "+bloqueo+", el jugador "+str(a+1)+" da vuelta una carta") #La acción no se realiza, pierde las monedas
                        self.extortion(against)
                        self.show_card(a+1,action_number)
                        print("El jugador "+str(j+1)+" devuelve su carta al mazo y saca otra")
                        return 1,j
                elif self.player[j]._Players__influence2 == blocking_card:
                        print("El jugador "+str(j+1)+" posee la influencia "+bloqueo+", el jugador "+str(a+1)+" da vuelta una carta") #La acción no se realiza, pierde las monedas
                        self.extortion(against)
                        self.show_card(a+1,action_number)
                        print("El jugador "+str(j+1)+" devuelve su carta al mazo y saca otra")
                        return 2,j
                elif self.player[j]._Players__influence1 == blocking_card2:
                        print("El jugador "+str(j+1)+" posee la influencia "+bloqueo2+", el jugador "+str(a+1)+" da vuelta una carta") #La acción no se realiza, pierde las monedas
                        self.extortion(against)
                        self.show_card(a+1,action_number)
                        print("El jugador "+str(j+1)+" devuelve su carta al mazo y saca otra")
                        return 1,j
                elif self.player[j]._Players__influence2 == blocking_card2:
                        print("El jugador "+str(j+1)+" posee la influencia "+bloqueo2+", el jugador "+str(a+1)+" da vuelta una carta") #La acción no se realiza, pierde las monedas
                        self.extortion(against)
                        self.show_card(a+1,action_number)
                        print("El jugador "+str(j+1)+" devuelve su carta al mazo y saca otra")
                        return 2,j
            else:       
                print("Nadie desafió el contra-ataque")  #En el caso de que nadie haya querido desafiar el contra-ataque, la acción se anula y no pasa nada
                if action_number == 1:
                    self.player[self.__i]._Players__coins -= 3 #pierde las monedas
                return 0,0

        else:
            self.extortion(against)  #En el caso de que ya les hayan preguntado a todos y nadie haya querido contraatacar
            return 0,0

    def block_card(self,action_number):
        challenge  = []
        attack = []
        if action_number == 1:
            against = self.murder()
            bloqueo = "CONDESA"
            accion = "ASESINATO"
            action_card = "A"
            blocking_card = "Co"

        for j in range(0, len(self.__player)):
            if j != self.i:
                print("\nJugador "+str(j+1)+", elija una opción.")
                print("1. POSEO LA CARTA "+bloqueo +" Y QUIERO CONTRA-ATACAR",accion, " DEL JUGADOR ",str(self.__i+1))
                print("2. DESAFIAR A JUGADOR "+str(self.__i+1))
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
                self.show_card(self.__i+1, action_number)      #Como no posee la influencia, la acción no se realiza, no gasta monedas
                return 0, 0
            
            elif self.player[self.__i]._Players__influence1 == action_card:
                print("El jugador "+str(self.__i +1)+" posee la influencia "+action_card + ", el jugador "+str(j+1)+" da vuelta una carta")
                self.show_card(j+1,action_number)
                print("El jugador "+str(self.__i +1)+" devuelve su carta al mazo y saca otra")
                self.make_murder(against, action_number)         #Como posee la influencia, la acción se realiza al jugador elegido
                return 1, self.__i

            elif self.player[self.__i]._Players__influence2 == action_card:
                print("El jugador "+str(self.__i +1)+" posee la influencia "+action_card + ", el jugador "+str(j+1)+" da vuelta una carta")
                self.show_card(j+1,action_number)
                print("El jugador "+str(self.__i +1)+" devuelve su carta al mazo y saca otra.")
                self.make_murder(against,action_number)         #Como posee la influencia, la acción se realiza
                return 2, self.__i
        #FALTAN LOS CONRAATAQUES
        if len(attack) > 0:
            selected_attack = random.randint(0,len(attack)-1)
            j = attack[selected_attack]
            print("--------------El jugador "+ str(j+1) +" realiza un contra-ataque a jugador "+str(self.i+1)+"-------------")
            for a in range(0, len(self.__player)):
                if a != j:
                    print("\nJugador "+str(a+1)+", elija una opción.")
                    print("\n1. DESAFIAR A JUGADOR", j+1)
                    print("0. NO HACER NADA")
                    b = int(input())
                    if b == 1:
                        challenge.append(a)
            if len(challenge) >0:           #si alguien quiso desafiar
                selected_challenge = random.randint(0,len(challenge)-1)
                a = challenge[selected_challenge]
                print("--------------El jugador "+str(a+1)+" realiza un desafío a jugador "+str(j+1)+"-------------")
                if self.player[j]._Players__influence1 != blocking_card and self.player[j]._Players__influence2 != blocking_card:
                        print("El jugador "+str(j+1)+" no posee la influencia "+bloqueo+", da vuelta una carta")
                        self.show_card(j+1,action_number) #La acción se realiza porque el contraataque fue falso
                        if action_number == 1:
                            self.make_murder(against,action_number)
                        return 0, 0
                elif self.player[j]._Players__influence1 == blocking_card:
                        print("El jugador "+str(j+1)+" posee la influencia "+bloqueo+", el jugador "+str(a+1)+" da vuelta una carta") #La acción no se realiza, pierde las monedas
                        if action_number == 1:
                            self.player[self.__i]._Players__coins -= 3
                        self.show_card(a+1,action_number)
                        print("El jugador "+str(j+1)+" devuelve su carta al mazo y saca otra")
                        return 1,j
                elif self.player[j]._Players__influence2 == blocking_card:
                        print("El jugador "+str(j+1)+" posee la influencia "+bloqueo+", el jugador "+str(a+1)+" da vuelta una carta") #La acción no se realiza, pierde las monedas
                        if action_number == 1:
                            self.player[self.__i]._Players__coins -= 3
                        self.show_card(a+1,action_number)
                        print("El jugador "+str(j+1)+" devuelve su carta al mazo y saca otra")
                        return 2,j
            else:       
                print("Nadie desafió el contra-ataque")  #En el caso de que nadie haya querido desafiar el contra-ataque, la acción se anula y no pasa nada
                if action_number == 1:
                    self.player[self.__i]._Players__coins -= 3 #pierde las monedas
                return 0,0

        else:
            if action_number == 1:
                self.make_murder(against,action_number)  #En el caso de que ya les hayan preguntado a todos y nadie haya querido contraatacar
            return 0,0

    def make_murder(self,against,action_number):
        self.player[self.__i]._Players__coins -= 3
        print("Se realiza el asesinato al jugador"+str(against))
        self.show_card(against, action_number)
