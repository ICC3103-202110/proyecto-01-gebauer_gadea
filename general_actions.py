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
        challenge = []
        attack = []
        for j in range(0, len(self.__player)): #Hay que buscar la forma de saber la cantidad de jugadores que juegan
            if j != self.i:
                print("\nJugador "+str(j+1)+", elija una opción.")
                print("\n1. POSEO EL DUQUE Y QUIERO CONTRA-ATACAR AYUDA DEL EXTRANJERO DE JUGADOR", self.i+1)
                print("0. NADA\n")
                a = int(input())
                if a == 1:  #Si alguien quiere contraatacar..
                    attack.append(j)
                    


                elif a !=0 and a != 1:
                    print("Esa opción no es correcta, se asimila que no quiere hacer nada")
                    a = 0
        if len(attack) >0:    #si alguien quiso contra-atacar....
            selected_attack = random.randint(0,len(attack)-1)  #Se elije un contra-ataque al azar de los que decidieron contra-atacar
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
                if self.player[j]._Players__influence1 != "D" and self.player[j]._Players__influence2 != "D":
                        print("El jugador "+str(j+1)+" no posee la influencia Duque, da vuelta una carta")
                        self.show_card(j+1,2)
                        return 0
                elif self.player[j]._Players__influence1 == 'D':
                        print("El jugador "+str(j+1)+" posee la influencia Duque, el jugador "+str(a+1)+" da vuelta una carta")
                        self.show_card(a+1,2)
                        print("El jugador "+str(j+1)+" devuelve su carta al mazo y saca otra")
                        return 1,j
                elif self.player[j]._Players__influence2 == 'D':
                        print("El jugador "+str(j+1)+" posee la influencia Duque, el jugador "+str(a+1)+" da vuelta una carta")
                        self.show_card(a+1,2)
                        print("El jugador "+str(j+1)+" devuelve su carta al mazo y saca otra")
                        return 2,j
            else:       
                print("Nadie desafió el contra-ataque")  #En el caso de que nadie haya querido desafiar el contra-ataque, la acción se anula y no pasa nada
                return 0 
        else:
            self.player[self.__i]._Players__coins+= 2  #En el caso de que ya les hayan preguntado a todos y nadie haya querido contraatacar
            return 0


    def hit(self):
        against = int(input("Elija un jugador al que quiera realizar esta acción"))
        if against ==  self.__i+1:
            print("No puede hacérselo a usted mismo")
            self.hit()
        elif against <1 or against > self.__player:
            print("No existe ese jugador")
            self.hit()
        else: 
            hit = 3
            self.player[self.__i]._Players__coins -=7
            self.show_card(against,hit)


 
    def show_card(self,against,accion):
        if self.player[against-1]._Players__seen_cards1 != str([]) and (self.player[against-1]._Players__seen_cards2 != str([])):
            print("Ese jugador ya tiene sus cartas dadas vuelta. Ya perdió. Elija otro")
            if accion == 3:
                self.hit()
            elif accion == 2:
                self.abroad_help()
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