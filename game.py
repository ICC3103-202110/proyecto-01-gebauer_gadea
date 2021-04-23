#esta deberia crear los menus tanto de acciones iniciales como contraataques o desafios
#ademas aca se deberia crear el maso de cartas

class Game:
    def __init__(self,player,players_list):
        self.__player = player
        self.__players_list = players_list

    @property
    def player(self):
        return self.__player

    @property
    def players_list(self):
        return self.__players_list  


    def print_menu(self):
            self.shown_cards()
            self.show_coins()
            print("------------------")
            print("Le toca al jugador", self.__player+1)
            print("------------------")
            print("\nQuiere ver sus cartas? s/n")
            see = str(input())
            if see == "s":
                print(f"Sus cartas son => {self.__players_list[self.__player]._Players__influence1},{self.__players_list[self.__player]._Players__influence2}")
            if see != "n" and see !="s":
                print("Respuesta incorrecta. Se asume que no quiere ver sus cartas")
            if self.__players_list[self.__player].coins == 10:
                print("Tiene 10 monedas, elije la acción golpe")
                return 3
            else:
                print("\nINGRESE UNA OPCION:")
                print("1. Ingreso")
                print("2. Ayuda del extranjero")
                print("3. Golpe")
                print("4. Impuesto(D)")
                print("5. Asesinato(A)")
                print("6. Extorsion(Ca)")
                print("7. Cambio(E))")
                answer = int(input())
                if answer<1 or answer>7:
                    print("Valor no valido. Trate otra vez")
                    self.print_menu() 
                else:
                    return answer

    def shown_cards(self):
        print("\nCartas de jugadores\n")
        for (i,_) in enumerate(self.__players_list):
            if self.__players_list[i]._Players__player_number != 0:
                print(f"player {self.__players_list[i]._Players__player_number} => {self.__players_list[i]._Players__seen_cards1} {self.__players_list[i]._Players__seen_cards2}\n")
            
    def show_coins(self):
        print("\nMonedas de jugadores\n")
        for (i,_) in enumerate(self.__players_list):
            if self.__players_list[i]._Players__player_number != 0:
                print(f"player{self.__players_list[i]._Players__player_number} => {self.__players_list[i]._Players__coins},{self.__players_list[i]._Players__influence1},{self.__players_list[i]._Players__influence2}")
    