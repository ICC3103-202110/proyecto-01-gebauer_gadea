import random
#primero pregunta cantidad de jugadores
from cards import Cards
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
    card1 = select_influence()
    card2 = select_influence()
    for i in range(0,players_num):
        p = Cards(str(i+1),card1,card2)
        players.append(p)


def show_cards():
    print("\nJugadores y cartas ")
    for (i,_) in enumerate(players):
        print(f"{i}: {players[i].player_number}-{players[i].influence1}-{players[i].influence2}")


if __name__ == '__main__':   
    create_game()

