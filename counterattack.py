#esta es la clase de la acion de contraatacar
# esta deberia recibir los 2 jugadores invlucrados la accion contraatacada y las 4 influencias
#esta al fin y al cabo es parecida a las acciones pero si se ejecutan bien bloquea la accion inicial
import random

class Counter_attack:
    def __init__(self,player, players_list,action):
        self.__player = player   #El que está jugando
        self.__players_list = players_list
        self.__action = action

    @property
    def player(self):
        return self.__player

    @property
    def players_list(self):
        return self.__players_list

    @property
    def action(self):
        return self.__action


    def blocking_card(self):
        if self.__action == 2:
            block_card = ["D",0]
            names = ["DUQUE",0]
            action = "AYUDA DEL EXTRANJERO"
        elif self.__action == 5:
            block_card = ["Co",0]
            names = ["CONDESA",0]
            action = "ASESINATO"
        elif self.__action == 6:
            block_card = ["E","Ca"]
            names = ["EMBAJADOR","CAPITÁN"]
            action = "EXTORSIÓN"
        return block_card ,names,action

        



    def ask_players(self):
        block_card,names,action = self.blocking_card()
        attack = []
        for j in range(0, len(self.__players_list)): #Hay que buscar la forma de saber la cantidad de jugadores que juegan
            if j != self.__player:
                if self.__players_list[j]._Players__player_number != 0:
                    print("\nJugador "+str(j+1)+", elija una opción.")
                    if block_card[0] == "D" or block_card[0] == "Co":
                        print("\n1. POSEO LA CARTA "+str(names[0])+" Y QUIERO CONTRA-ATACAR LA ACCIÓN "+action)
                    else:
                        print("\n1. POSEO LA CARTA "+str(names[0])+" Ó "+str(names[1])+" Y QUIERO CONTRA-ATACAR LA ACCIÓN "+action)
                    print("0. NADA\n")
                    a = int(input())
                    if a == 1:  #Si alguien quiere contraatacar..
                        attack.append(j)
                    elif a !=0 and a != 1:
                        print("Esa opción no es correcta, se asimila que no quiere hacer nada")
                        a = 0
        if len(attack) == 0:
            return 0
        else:
            return attack

    def attack(self):
        attack = self.ask_players() #lista de contra-ataques
        if attack == 0:
            return 0         #Se devuelve 0 si nadie quiso contraatacar, entonces la acción se puede realizar
        else:
            selected_attack = random.randint(0,len(attack)-1)  #Se elije un contra-ataque al azar de los que decidieron contra-atacar
            j = attack[selected_attack]
            print("--------------El jugador "+ str(j+1) +" realiza un contra-ataque a jugador "+str(self.__player+1)+"-------------")
        return j+1   #Se devuelve el jugador que quiso contra-atacar