import random
from game import Game
from players import Players
from entry import Entry
from abroad_help import Abroad_help
from hit import Hit
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
        if selection ==1:
            action = Entry(players,p_counter)
            action.a_entry()
            change_player(p_counter)
        elif selection ==2:
            action = Abroad_help(players,p_counter)
            action.a_entry()
            change_player(p_counter)
        elif selection ==3:
            action = Hit(players,p_counter)
            action.hit()
            change_player(p_counter)
        elif selection == 4:
            change_player(p_counter)
        elif selection ==5:
            change_player(p_counter)
        elif selection ==6:
            change_player(p_counter)
        elif selection == 7:
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
    
    