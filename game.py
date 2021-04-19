#esta deberia crear los menus tanto de acciones iniciales como contraataques o desafios
#ademas aca se deberia crear el maso de cartas

class Game:
    def __init__(self,player,players_list):
        self.player = player
        self.players_list = players_list




    def print_menu(self):
            self.shown_cards
            self.show_coins()
            print("------------------")
            print("Le toca al jugador", self.player+1)
            print("------------------")
            print("\nQuiere ver sus cartas? s/n")
            see = str(input())
            if see == "s":
                print(f"Sus cartas son => {self.players_list[self.player]._Players__influence1},{self.players_list[self.player]._Players__influence2}")
            if see != "n" and see !="s":
                print("Respuesta incorrecta. Se asume que no quiere ver sus cartas")
            if self.players_list[self.player].coins == 10:
                print("Tiene 10 monedas, elije la acción golpe")
                return 3
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
                    print("Valor no valido. Trate otra vez")
                    self.print_menu() 
                else:
                    return answer

    def shown_cards(self):
        print("\nCartas de jugadores\n")
        for (i,_) in enumerate(self.players_list):
            print(f"player{self.players_list[i]._Players__player_number} => {self.players_list[i]._Players__seen_cards1} {self.players_list[i]._Players__seen_cards2}\n")
        
    def show_coins(self):
        print("\nMonedas de jugadores\n")
        for (i,_) in enumerate(self.players_list):
            print(f"player{self.players_list[i]._Players__player_number} => {self.players_list[i]._Players__coins},{self.players_list[i]._Players__influence1},{self.players_list[i]._Players__influence2}")
    