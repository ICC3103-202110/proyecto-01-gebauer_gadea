#este es la ejecucion de el desafio 
#este deberia recibir los dos jugadores y las 4 cartas respectivamente y usa el modulo de las clases de tipos de cartas para verificar quien gana
import random
class Challenge:
    def __init__(self,player,players_list,action):
        self.player = player   #El que está jugando
        self.players_list = players_list
        self.action = action

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
        action_name, influence_needed, influence_name,block_card,names = self.cards()
        challenge_list = []
        for a in range(0, len(self.players_list)):
            if a != self.player:
                    print("\nJugador "+str(a+1)+", elija una opción.")
                    print("\n1. DESAFIAR A JUGADOR", self.player)
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
        if challenges == 0:
            return 0 #NADIE QUISO DESAFIAR, LA ACCIÓN NO SE HACE
        else:
                selected_challenge = random.randint(0,len(challenges)-1)
                a = challenges[selected_challenge]
                print("--------------El jugador "+str(a+1)+" realiza un desafío a jugador "+str(self.player+1)+"-------------")
                if self.action == 4 or self.action == 5 or self.action == 6 or self.action == 7:
                    print("Falta")
                else:
                    if self.players_list[self.player]._Players__influence1 != "D" and self.players_list[self.player]._Players__influence2 != "D":
                        print("El jugador "+str(self.player+1)+" no posee la influencia Duque, da vuelta una carta")
                        self.players_list[self.player]._Players__coins+= 2
                        self.show_card(self.player+1,2)
                        return 3     #EL QUE CONTRA-ATACÓ MINTIÓ, ENTONCES SI SE HACE LA ACCIÓN Y RETORNA 3               
                    elif self.players_list[self.player]._Players__influence1 == 'D':
                        print("El jugador "+str(self.player+1)+" posee la influencia Duque, el jugador "+str(a+1)+" da vuelta una carta")
                        self.show_card(a+1,2)
                        print("El jugador "+str(self.player+1)+" devuelve su carta al mazo y saca otra")
                        return 1         #SE REALIZA EL CONTRAATACQUE, EL QUE DESAFIÓ PERDIÓ
                    elif self.players_list[self.player]._Players__influence2 == 'D':
                        print("El jugador "+str(self.player+1)+" posee la influencia Duque, el jugador "+str(a+1)+" da vuelta una carta")
                        self.show_card(a+1,2)   
                        print("El jugador "+str(self.player+1)+" devuelve su carta al mazo y saca otra")
                        return 2              #SE REALIZA EL CONTRAATAQUE, EL QUE DESAFIÓ PERDIÓ


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