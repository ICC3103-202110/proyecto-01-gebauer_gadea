#este es la ejecucion de el desafio 
#este deberia recibir los dos jugadores y las 4 cartas respectivamente y usa el modulo de las clases de tipos de cartas para verificar quien gana
import random
class Challenge:
    def __init__(self,player,players_list,time,action):
        self.__player = player   #El que está jugando
        self.__players_list = players_list
        self.__action = action
        self.__time = time

    @property
    def player(self):
        return self.__player

    @property
    def players_list(self):
        return self.__players_list

    @property
    def action(self):
        return self.__action
    
    @property
    def time(self):
        return self.__time

    def cards(self):
        if self.__action == 2:
            block_card = ["D",0]   #En este caso, se desafía el contra-ataque (carta D)
            names = ["DUQUE",0]
            action_name = "AYUDA DEL EXTRANJERO"
            influence_needed = 0
            influence_name = 0
        elif self.__action == 4:
            influence_needed = "D"
            influence_name = "DUQUE"
            block_card = [0,0]
            names = [0,0]
            action_name = "IMPUESTO"
        elif self.__action == 5:
            block_card = ["Co",0]
            names = ["CONDESA",0]
            influence_needed = "A"
            influence_name = "ASESINO"
            action_name = "ASESINATO"
        elif self.__action == 6:
            influence_needed = "Ca"
            influence_name = "CAPITÁN"
            block_card = ["E","Ca"]
            names = ["EMBAJADOR","CAPITÁN"]
            action_name = "EXTORSIÓN"
        elif self.__action == 7:
            influence_needed = "E"
            influence_name = "EMBAJADOR"
            block_card = [0,0]
            names = [0,0]
            action_name = "EXTORSIÓN"
        return action_name, influence_needed, influence_name,block_card,names


    def ask_players(self):
        challenge_list = []
        for a in range(0, len(self.__players_list)):
            if a != self.__player:
                if self.__players_list[a]._Players__player_number != 0:
                    print("\nJugador "+str(a+1)+", elija una opción.")
                    print("\n1. DESAFIAR A JUGADOR", self.__player+1)
                    print("0. NO HACER NADA")
                    b = int(input())
                    if b == 1:
                        challenge_list.append(a)

        if len(challenge_list) == 0:
            return 0
        else:
            return challenge_list

    def challenge_player(self):
        challenges = self.ask_players()
        action_name, influence_needed, influence_name,block_card,names = self.cards()
        if challenges == 0:
            return 0,0,0 #NADIE QUISO DESAFIAR, LA ACCIÓN SE HACE O PASA A CONTRA-ATAQUE
        else:
                selected_challenge = random.randint(0,len(challenges)-1)
                a = challenges[selected_challenge]
                print("--------------El jugador "+str(a+1)+" realiza un desafío a jugador "+str(self.__player+1)+"-------------")

                if self.__time == 1:

                    if self.__players_list[self.__player]._Players__influence1 != influence_needed and self.__players_list[self.__player]._Players__influence2 != influence_needed:
                        print("El jugador "+str(int(self.player)+1)+" no posee la influencia "+str(influence_name)+", da vuelta una carta")
                        self.show_card(self.__player+1)
                        return 0,1,0    #El jugador pierde el desafío porque no tiene la influencia, la acción no se realiza
                    elif self.__players_list[self.__player]._Players__influence1 == influence_needed:
                        print("El jugador "+str(self.__player +1)+" posee la influencia "+influence_needed + ", el jugador "+str(a+1)+" da vuelta una carta") #Si posee, la influencia, si hace la acción
                        self.show_card(a+1)
                        print("El jugador "+str(self.__player +1)+" devuelve su carta al mazo y saca otra.")
                        return 1,3,0   #Devuelve la carta 1 , sigue al contra-ataque

                    elif self.__players_list[self.__player]._Players__influence2 == influence_needed:
                        print("El jugador "+str(self.__player +1)+" posee la influencia "+influence_needed + ", el jugador "+str(a+1)+" da vuelta una carta")
                        self.show_card(a+1)
                        print("El jugador "+str(self.__player +1)+" devuelve su carta al mazo y saca otra.")
                        return 2,3, 0 #Devuelve la carta2,  sigue el contra-ataque
                else:
                    if self.__action != 6:
                        if self.__players_list[self.__player]._Players__influence1 != block_card[0] and self.__players_list[self.__player]._Players__influence2 !=block_card[0]:
                            print("El jugador "+str(self.player+1)+" no posee la influencia "+ names[0]+", da vuelta una carta")
                            self.show_card(self.__player+1)
                            return 0,1,0    #El jugador pierde el desafío entonces no puede hacer el contra-ataque
                        elif self.players_list[self.__player]._Players__influence1 == block_card[0]:
                            print("El jugador "+str(self.__player +1)+" posee la influencia "+ names[0] + ", el jugador "+str(a+1)+" da vuelta una carta") #Si posee, la influencia, si hace la acción
                            self.show_card(a+1)
                            print("El jugador "+str(self.__player +1)+" devuelve su carta al mazo y saca otra.")
                            return 1,3, a   #Devuelve la carta 1 , sigue al contra-ataque

                        elif self.__players_list[self.__player]._Players__influence2 == block_card[0]:
                            print("El jugador "+str(self.__player +1)+" posee la influencia "+names[0] + ", el jugador "+str(a+1)+" da vuelta una carta")
                            self.show_card(a+1)
                            print("El jugador "+str(self.__player +1)+" devuelve su carta al mazo y saca otra.")
                            return 2,3, a  #Devuelve la carta2,  sigue el contra-ataque

                    else:
                        if self.__players_list[self.___player]._Players__influence1 != block_card[0] and self.__players_list[self.___player]._Players__influence2 !=block_card[1] and self.__players_list[self.__player]._Players__influence2 !=block_card[1]:
                            print("El jugador "+str(self.player+1)+" no posee la influencia "+ names[0]+" ni " +names[1]+", da vuelta una carta")
                            self.show_card(self.__player+1) #La acción se realiza porque el contraataque fue falso
                            return 0, 1, 0
                        elif self.__players_list[self.__player]._Players__influence1 == block_card[0]:
                            print("El jugador "+str(self.__player+1)+" posee la influencia "+names[0]+", el jugador "+str(a+1)+" da vuelta una carta") #La acción no se realiza, pierde las monedas
                            self.show_card(a+1)
                            print("El jugador "+str(self.__player+1)+" devuelve su carta al mazo y saca otra")
                            return 1,self.__player+1,0
                        elif self.__players_list[self.__player]._Players__influence2 == block_card[0]:
                            print("El jugador "+str(self.__player+1)+" posee la influencia "+names[0]+", el jugador "+str(a+1)+" da vuelta una carta") #La acción no se realiza, pierde las monedas
                            self.show_card(a+1)
                            print("El jugador "+str(self.__player+1)+" devuelve su carta al mazo y saca otra")
                            return 2,self.__player+1, 0
                        elif self.__players_list[self.__player]._Players__influence1 == block_card[1]:
                            print("El jugador "+str(self.__player+1)+" posee la influencia "+names[1]+", el jugador "+str(a+1)+" da vuelta una carta") #La acción no se realiza, pierde las monedas
                            self.show_card(a+1)
                            print("El jugador "+str(self.__player+1)+" devuelve su carta al mazo y saca otra")
                            return 1,self.player+1,0 
                        elif self.__players_list[self.__player]._Players__influence2 == block_card[1]:
                            print("El jugador "+str(self.__player+1)+" posee la influencia "+names[1]+", el jugador "+str(a+1)+" da vuelta una carta") #La acción no se realiza, pierde las monedas
                            self.show_card(a+1)
                            print("El jugador "+str(self.__player+1)+" devuelve su carta al mazo y saca otra")
                            return 2,self.__player+1,0



    def show_card(self,against):
        print("Jugador", (against))
        if self.__players_list[against-1]._Players__seen_cards1 != str([]):
            print("Sólo le queda una carta, se dará vuelta esa")
            print("JUGADOR " +str(against)+ " PIERDE EL JUEGO")
            self.__players_list[against-1]._Players__player_number = 0
            card = 2  
        elif self.players_list[against-1]._Players__seen_cards2 != str([]):
            print("Sólo le queda una carta, se dará vuelta esa")
            print("JUGADOR " +str(against)+ " PIERDE EL JUEGO")
            self.__players_list[against-1]._Players__player_number = 0
            card = 1
        else:
            card = int(input("Diga la carta que quiera dar vuelta(1 o 2)"))
        if card != 1 and card != 2 :
            print("Esa carta no existe. Se elijirá al azar")
            card = random.randint(1,2)
        if card == 1:
            self.__players_list[against-1]._Players__seen_cards1 = "["+str(self.__players_list[against-1]._Players__influence1)+"]"
        else:
            self.__players_list[against-1]._Players__seen_cards2 = "["+str(self.__players_list[against-1]._Players__influence2)+"]"

