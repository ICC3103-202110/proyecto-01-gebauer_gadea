import random
from game import Game
from players import Players
from entry import Entry
from challenge import Challenge
from abroad_help import Abroad_help
from hit import Hit
from counterattack import Counter_attack
from tax import Tax
from change import Change
from murderer import Murder

players = []
influences = []
posibilities_names = ["D","A","Ca","Co","E"]

def create_game():
    for i in posibilities_names:
        for j in range(0,players_num):
            influences.append(i)
    random.shuffle(influences)
    for i in range(0,players_num):
        card1 = select_influence()
        card2 = select_influence()
        players.append(Players(str(i+1),card1,card2,2))

def change_player(p_counter):
    if p_counter == len(players)-1:
        p_counter = 0
    else:
        p_counter += 1
    menu_options(p_counter)

def select_influence():
    card = influences[0]
    influences.pop(0)
    return card

def player_turn(p_counter):
    game_actions = Game(p_counter,players)
    answer = game_actions.print_menu()
    return answer



def menu_options(p_counter):
    while True:
        selection = player_turn(p_counter)
        if selection ==1:                   #LISTO
            action = Entry(players,p_counter)
            action.a_entry()
            change_player(p_counter)
        elif selection ==2:     #LISTO
            block = Counter_attack(p_counter,players,2)
            block = block.attack()
            if block == 0:           #Nadie quiso contraatacar, entonces se ejecuta la acción.
                action = Abroad_help(players,p_counter)
                action.a_entry()
            else:                                       #En este caso se puede hacer un desafío
                attacking = block                  #El jugador "block" quiso contraatacar
                action = Challenge(attacking, players,1,2)
                attack = action.challenge_player()
                if attack == 0:                       #Nadie quiso desafiar el contra-ataque, entonces no se ejecuta la acción y le toca al siguiente jugador
                    change_player(p_counter)
                elif attack == 3:              #El que contra-atacó mintió, la acción si se ejecuta
                    action = Abroad_help(players,p_counter)
                    action = action.a_entry
                elif attack == 1:
                        players[attacking]._Players__influence1 = return_card(players[attacking]._Players__influence1)  
                elif attack == 2:
                    players[attacking]._Players__influence2 = return_card(players[attacking]._Players__influence2)
            change_player(p_counter)


        elif selection ==3:                   #LISTO
            action = Hit(players,p_counter)
            action.hit()
            change_player(p_counter)

        elif selection == 4:       #LISTO
            action = Challenge(p_counter,players,1,4)  #El 1 significa que se verifican las influencias de acciones
            a, b= action.challenge_player()
            if a == 0 and b == 0:     #Nadie quiso desafiar, entonces se ejecuta la acción
                action = Tax(players, p_counter)
                action.a_tax()
            elif b == 3:
                if a == 1:
                    players[p_counter]._Players__influence1 = return_card(players[p_counter]._Players__influence1) 
                elif a == 2:
                    players[p_counter]._Players__influence2 = return_card(players[p_counter]._Players__influence2)
            change_player(p_counter) 
    


        elif selection ==5:      #ASESINATO---------------
            action = Challenge(p_counter,players,1,5)
            a, b, c= action.challenge_player()
            if a == 0 and b == 0:     #Nadie quiso desafiar, luego van los contra-ataques
                action = Counter_attack(p_counter,players,5)
                player_attack = action.attack()
                if player_attack == 0:      #Nadie quiso contra-atacar ni desafiar, entonces se ejecuta la acción
                    action = Murder(players, p_counter)
                    action.murder()
                else:                    #Nadie quiso desafiar pero si contra-atacar, se pregunta si desafían al que contra-atacó (supuestamente tiene a la Condesa)
                    action = Challenge(player_attack-1,players,2,5)
                    a, b , c = action.challenge_player()  #c es el jugador que desafió
                    if a == 0 and b == 0:   #Nadie desafía el contra-ataque, la acción no se cumple
                        change_player(p_counter)
                    elif a == 0 and b == 1:  #Pierde el desafío el que contra-atacó, se ejecuta la acción
                        action = Murder(players, p_counter)
                        action.murder()
                    elif b == 3:          #El que contraatacó ganó el desafío.
                        if a == 1:
                            players[c]._Players__influence1 = return_card(players[c]._Players__influence1)
                        else:
                            players[c]._Players__influence2 = return_card(players[c]._Players__influence2)
                    

            elif a == 0 and b ==1:    #Alguien quiso contra-atacar, el jugador pierde el desafío entonces no realiza la acción y cambia de turno
                change_player(p_counter)
            elif b == 3:        #Si poseía la carta influencia, entonces pasa a contra-ataques
                if a == 1:
                    players[p_counter]._Players__influence1 = return_card(players[p_counter]._Players__influence1)
                elif a == 2:
                    players[p_counter]._Players__influence2 = return_card(players[p_counter]._Players__influence2)
                action = Counter_attack(p_counter,players,5)
                player_attack = action.attack()
                if player_attack == 0:      #Nadie quiso contra-atacar ni desafiar, entonces se ejecuta la acción
                    action = Murder(players, p_counter)
                    action.murder()
                else:                    #Nadie quiso desafiar pero si contra-atacar, se pregunta si desafían al que contra-atacó (supuestamente tiene a la Condesa)
                    action = Challenge(player_attack-1,players,2,5)
                    a, b , c = action.challenge_player()  #c es el jugador que desafió
                    if a == 0 and b == 0:   #Nadie desafía el contra-ataque, la acción no se cumple
                        change_player(p_counter)
                    elif a == 0 and b == 1:  #Pierde el desafío el que contra-atacó, se ejecuta la acción
                        action = Murder(players, p_counter)
                        action.murder()
                    elif b == 3:          #El que contraatacó ganó el desafío.
                        if a == 1:
                            players[c]._Players__influence1 = return_card(players[c]._Players__influence1)
                        else:
                            players[c]._Players__influence2 = return_card(players[c]._Players__influence2)

        elif selection ==6:    #EXTORSIÓN-------------
            action = Challenge(p_counter,players,1,6)
            a, b= action.challenge_player()
            if a == 0 and b == 0:     #Nadie quiso contra-atacar, luego van los contra-ataques
                print("hola.Faltan los contra-ataques")
            elif a == 0 and b ==1:    #el jugador pierde el desafío entonces no realiza la acción y cambia de turno
                change_player(p_counter)
            elif b == 3:        #Si poseía la carta influencia, pasa a contra-ataque
                if a == 1:
                    players[p_counter]._Players__influence1 = return_card(players[p_counter]._Players__influence1)
                elif a == 2:
                    players[p_counter]._Players__influence2 = return_card(players[p_counter]._Players__influence2)
            
        elif selection == 7:     #LISTA-------------
            action = Challenge(p_counter,players,1,7)
            a, b= action.challenge_player()
            if a == 0 and b == 0:     #Nadie quiso desafiar, entonces se hace la acción
                action = Change(players,p_counter,influences)
                action.change_cards()
            elif a == 0 and b ==1:    #el jugador pierde el desafío entonces no realiza la acción y cambia de turno
                change_player(p_counter)
            elif b == 3:        #Si poseía la carta influencia, realiza la acción
                if a == 1:
                    players[p_counter]._Players__influence1 = return_card(players[p_counter]._Players__influence1)
                elif a == 2:
                    players[p_counter]._Players__influence2 = return_card(players[p_counter]._Players__influence2)
                action = Change(players,p_counter,influences)
                action.change_cards()
                change_player(p_counter)

   
    
            

def return_card(carta):
    influences.append(carta)            #Devuelve la carta al mazo 
    random.shuffle(influences)          #Se mezcla el mazo
    return_card1 = influences[0]        #Toma una carta del mazo
    influences.pop(0)
    return return_card1




if __name__ == '__main__':

    p_counter = 0 
    players_num = 0
    while players_num != 3 and players_num != 4:
        players_num = int(input("\nElija la cantidad de jugadores (3 o 4)"))
    create_game()
    menu_options(p_counter)
    
    