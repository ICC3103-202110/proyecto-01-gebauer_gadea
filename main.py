import random
#primero pregunta cantidad de jugadores
from players import Players
from character_action import Character_actions
from general_actions import General_actions


players = []
influences = []
posibilities = ["D","A","Ca","Co","E"]


    
def select_influence():
    card = influences[0]
    influences.pop(0)
    return card
def show_coins():
    print("\nMonedas de jugadores\n")
    for (i,_) in enumerate(players):
        print(f"player{players[i]._Players__player_number} => {players[i]._Players__coins}")
    shown_cards()

def create_game():
    for i in posibilities:
        for j in range(0,players_num):
            influences.append(i)
    random.shuffle(influences)
    for i in range(0,players_num):
        card1 = select_influence()
        card2 = select_influence()
        players.append(Players(str(i+1),card1,card2,2))
    print("Duque = D\nAsesino = A\nCapitán = Ca\nEmbajador= E\nCondesa = Co\n")
    

def print_menu1(p_counter):
    show_coins()
    print("-------------------------------------")
    print("Le toca al jugador", int(p_counter)+1)
    print("-------------------------------------\n")
    if players[p_counter].coins == 10:                  ####
        print("Tiene 10 monedas. Toma la acción de golpe")######
        answer = 3                              ####
        return answer                           ####
    else:   
        print("INGRESE UNA OPCION:")
        print("1. Ingreso")
        print("2. Ayuda del extranjero")
        print("3. Golpe")
        print("4. Impuesto(D)")
        print("5. Asesinato(A)")
        print("6. Extorcion(Ca)")
        print("7. Cambio(E))")
        answer = int(input())
        if answer<1 or answer>7:
            print("Valor no valido")
            print_menu1(p_counter) 
        else:
            return answer




def menu1(p_counter, players_num):
    while True:
        selection = print_menu1(p_counter)
        if selection == 1:
            a=General_actions(players,p_counter)
            a.entry() 
            change_player(p_counter,players_num) 
        if selection == 2:
            a=General_actions(players,p_counter)
            a.abroad_help()
            change_player(p_counter,players_num)
        if selection ==3:
            if players[p_counter].coins < 7:
                print("No puede realizar la acción golpe porque le faltan monedas. Trate otra")
                menu1(p_counter, players_num)
            else:
                a= General_actions(players,p_counter)
                a.hit()
                change_player(p_counter,players_num)
        if selection == 4:
            print("4")
        if selection == 5:
            print("5")
        if selection == 6:
            print("6")
        if selection ==7:
            a= Character_actions(players,influences,p_counter)
            a.change()
            random.shuffle(influences)
            print(influences)
            change_player(p_counter,players_num)
            
            

def shown_cards():
    print("\nCartas de jugadores\n")
    for (i,_) in enumerate(players):
        print(f"player{players[i]._Players__player_number} => {players[i]._Players__seen_cards1} {players[i]._Players__seen_cards2}\n")

def change_player(p_counter, players_num):
    if p_counter == players_num-1:
        p_counter = 0
    else:
        p_counter += 1
    menu1(p_counter,players_num)







if __name__ == '__main__':
    p_counter = 0
    players_num = int(input("\nElija la cantidad de jugadores (3 o 4)"))
    create_game()
    menu1(p_counter, players_num)