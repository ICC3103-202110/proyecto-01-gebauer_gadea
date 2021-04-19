#este es la ejecucion de el desafio 
#este deberia recibir los dos jugadores y las 4 cartas respectivamente y usa el modulo de las clases de tipos de cartas para verificar quien gana
import random
class Challenge:
    def __init__(self,player,players_list,time,action):
        self.player = player   #El que está jugando
        self.players_list = players_list
        self.action = action
        self.time = time

    def cards(self):
        if self.action == 2:
            block_card = ["D",0]   #En este caso, se desafía el contra-ataque (carta D)
            names = ["DUQUE",0]
            action_name = "AYUDA DEL EXTRANJERO"
            influence_needed = 0
            influence_name = 0
        elif self.action == 4:
            influence_needed = "D"
            influence_name = "DUQUE"
            block_card = [0,0]
            names = [0,0]
            action_name = "IMPUESTO"
        elif self.action == 5:
            block_card = ["Co",0]
            names = ["CONDESA",0]
            influence_needed = "A"
            influence_name = "ASESINO"
            action_name = "ASESINATO"
        elif self.action == 6:
            influence_needed = "Ca"
            influence_name = "CAPITÁN"
            block_card = ["E","Ca"]
            names = ["EMBAJADOR","CAPITÁN"]
            action_name = "EXTORSIÓN"
        elif self.action == 7:
            influence_needed = "E"
            influence_name = "EMBAJADOR"
            block_card = [0,0]
            names = [0,0]
            action_name = "EXTORSIÓN"
        return action_name, influence_needed, influence_name,block_card,names


    def ask_players(self):
        challenge_list = []
        for a in range(0, len(self.players_list)):
            if a != self.player:
                    print("\nJugador "+str(a+1)+", elija una opción.")
                    print("\n1. DESAFIAR A JUGADOR", self.player+1)
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
                print("--------------El jugador "+str(a+1)+" realiza un desafío a jugador "+str(self.player+1)+"-------------")

                if self.time == 1:

                    if self.players_list[self.player]._Players__influence1 != influence_needed and self.players_list[self.player]._Players__influence2 != influence_needed:
                        print("El jugador "+str(int(self.player)+1)+" no posee la influencia "+str(influence_name)+", da vuelta una carta")
                        self.show_card(self.player+1, self.action)
                        return 0,1,0    #El jugador pierde el desafío porque no tiene la influencia, la acción no se realiza
                    elif self.players_list[self.player]._Players__influence1 == influence_needed:
                        print("El jugador "+str(self.player +1)+" posee la influencia "+influence_needed + ", el jugador "+str(a+1)+" da vuelta una carta") #Si posee, la influencia, si hace la acción
                        self.show_card(a+1,self.action)
                        print("El jugador "+str(self.player +1)+" devuelve su carta al mazo y saca otra.")
                        return 1,3,0   #Devuelve la carta 1 , sigue al contra-ataque

                    elif self.players_list[self.player]._Players__influence2 == influence_needed:
                        print("El jugador "+str(self.player +1)+" posee la influencia "+influence_needed + ", el jugador "+str(a+1)+" da vuelta una carta")
                        self.show_card(a+1,self.action)
                        print("El jugador "+str(self.player +1)+" devuelve su carta al mazo y saca otra.")
                        return 2,3, 0 #Devuelve la carta2,  sigue el contra-ataque
                else:
                    if self.action != 7:

                        if self.players_list[self.player]._Players__influence1 != block_card[0] and self.players_list[self.player]._Players__influence2 !=block_card[0]:
                            print("El jugador "+str(self.player+1)+" no posee la influencia "+ names[0]+", da vuelta una carta")
                            self.show_card(self.player+1, self.action)
                            return 0,1    #El jugador pierde el desafío entonces no puede hacer el contra-ataque
                        elif self.players_list[self.player]._Players__influence1 == block_card[0]:
                            print("El jugador "+str(self.player +1)+" posee la influencia "+ names[0] + ", el jugador "+str(a+1)+" da vuelta una carta") #Si posee, la influencia, si hace la acción
                            self.show_card(a+1,self.action)
                            print("El jugador "+str(self.player +1)+" devuelve su carta al mazo y saca otra.")
                            return 1,3, a   #Devuelve la carta 1 , sigue al contra-ataque

                        elif self.players_list[self.player]._Players__influence2 == block_card[0]:
                            print("El jugador "+str(self.player +1)+" posee la influencia "+names[0] + ", el jugador "+str(a+1)+" da vuelta una carta")
                            self.show_card(a+1,self.action)
                            print("El jugador "+str(self.player +1)+" devuelve su carta al mazo y saca otra.")
                            return 2,3, a  #Devuelve la carta2,  sigue el contra-ataque




    def show_card(self,against,accion):
        print("Jugador", (against))
        if self.players_list[against-1]._Players__seen_cards1 != str([]):
            print("Sólo le queda una carta, se dará vuelta esa")
            print("JUGADOR " +str(against)+ " PIERDE EL JUEGO")
            card = 2  
        elif self.players_list[against-1]._Players__seen_cards2 != str([]):
            print("Sólo le queda una carta, se dará vuelta esa")
            print("JUGADOR " +str(against)+ " PIERDE EL JUEGO")
            card = 1
        else:
            card = int(input("Diga la carta que quiera dar vuelta(1 o 2)"))
        if card != 1 and card != 2 :
            print("Esa carta no existe. Se elijirá al azar")
            card = random.randint(1,2)
        if card == 1:
            self.players_list[against-1]._Players__seen_cards1 = "["+str(self.players_list[against-1]._Players__influence1)+"]"
        else:
            self.players_list[against-1]._Players__seen_cards2 = "["+str(self.players_list[against-1]._Players__influence2)+"]"