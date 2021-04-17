#PREGUNTAS PARA AYUDANTE:
#1) Cómo hacer una clase padre que tenga los atributos de general_actiones y character_actions (son los mismos atributos)
#2) Las 2 clases comparten el método de show_card()
#3) No entiendo en el caso de las acciones generales qué pasa con la acción cuando el que desafiaba pierde.

import random
from players import Players
from general_actions import General_actions
from character_action import Character_actions

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
        print(f"player{players[i]._Players__player_number} => {players[i]._Players__coins},{players[i]._Players__influence1},{players[i]._Players__influence2}")
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
    print("\nQuiere ver sus cartas? s/n")
    see = str(input())
    if see == "s":
        print(f"Sus cartas son => {players[p_counter]._Players__influence1},{players[p_counter]._Players__influence2}")
    if see != "n":
        print("Respuesta incorrecta. Se asume que no quiere ver sus cartas")
    if players[p_counter].coins == 10:                  ####
        print("Tiene 10 monedas. Toma la acción de golpe")######
        answer = 3                              ####
        return answer                           ####
    else:   
        print("\nINGRESE UNA OPCION:")
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
            b,j = a.abroad_help()
            if b == 1:
                players[j]._Players__influence1 = return_card(players[j]._Players__influence1)  
            elif b == 2:
                players[j]._Players__influence2 = return_card(players[j]._Players__influence2)
               
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


def return_card(carta):
    influences.append(carta)            #Devuelve la carta al mazo 
    random.shuffle(influences)          #Se mezcla el mazo
    return_card1 = influences[0]        #Toma una carta del mazo
    influences.pop(0)
    return return_card1




if __name__ == '__main__':
    p_counter = 0
    players_num = int(input("\nElija la cantidad de jugadores (3 o 4)"))
    create_game()
    menu1(p_counter, players_num)