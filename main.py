import random
#primero pregunta cantidad de jugadores
from players import Players
players = []
influences = []
posibilities = ["D","A","Ca","Co","E"]


    
def select_influence():
    card = influences[0]
    influences.pop(0)
    return card
def show_coins():
    print("Monedas de jugadores")
    for (i,_) in enumerate(players):
        print(f"player{players[i].player_number} => {players[i].coins}")

def create_game():
    players_num = int(input("\nElija la cantidad de jugadores (3 o 4)"))
    for i in posibilities:
        for j in range(0,players_num):
            influences.append(i)
    random.shuffle(influences)
    for i in range(0,players_num):
        card1 = select_influence()
        card2 = select_influence()
        players.append(Players(str(i+1),card1,card2,2))
    print("Duque = D\nAsesino = A\nCapitán = Ca\nEmbajador= E\nCondesa = Co\n")

def print_menu1():
    
    show_coins()
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
        print_menu1() 
    else:
        return answer

def menu1():
    create_game()
    while True:
        selection = print_menu1()
        if selection == 1:
            print("1")
        if selection == 2:
            print("2")
        if selection ==3:
            print("3")
        if selection == 4:
            print("4")
        if selection == 5:
            print("5")
        if selection == 6:
            print("6")
        if selection ==7:
            print("7")









if __name__ == '__main__':
    menu1()

