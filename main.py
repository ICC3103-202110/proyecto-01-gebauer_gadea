import random
#primero pregunta cantidad de jugadores
from players import Players
players = []
influences = []
posibilities = ["D","A","Ca","Co","E"]
print("Duque = D\nAsesino = A\nCapitán = Ca\nEmbajador= E\nCondesa = Co")

    
def select_influence():
    card = influences[0]
    influences.pop(0)
    return card

def create_game():
    players_num = int(input("Elija la cantidad de jugadores (3 o 4)"))
    for i in posibilities:
        for j in range(0,players_num):
            influences.append(i)
    random.shuffle(influences)
    for i in range(0,players_num):
        card1 = select_influence()
        card2 = select_influence()
        players.append(Players(str(i+1),card1,card2,2))


def show_cards():
    print("\nJugadores y cartas ")
    for (i,_) in enumerate(players):
        print(f"{i}: {players[i].player_number} - {players[i].influence1} - {players[i].influence2} - {players[i].coins}")


if __name__ == '__main__':   
    create_game()
    show_cards()

