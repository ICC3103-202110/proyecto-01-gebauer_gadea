#esta es la accion de cambio 
import random
class Change:

    #CONSTRUCTOR
    def __init__(self,player,i,influences):

        self.player = player
        self.i = i
        self.influences = influences

    def select_card(self):
        card1 = self.influences[0]
        card2 = self.influences[1]
        return card1, card2


    def change_cards(self):
        card1, card2 = self.select_card()
        list1 = [card1,card2,self.player[self.i]._Players__influence1,self.player[self.i]._Players__influence2]
        print("ACCIÓN CAMBIAR CARTAS")
        print(f" 1:{list1[0]}  2:{list1[2]}  3:{list1[3]}  4:{list1[3]}")
        print("Elije la primera carta para quedarte")
        answer = int(input())
        print("Elije la segunda carta para quedarte")
        answer2 = int(input())
        if answer != 1 and answer != 2 and answer != 3 and answer != 4:
            print("Carta 1 incorrecta. Trate otra vez")
            self.change_cards()
        elif answer2 != 1 and answer2 != 2 and answer2 != 3 and answer2 != 4:
            print("Carta 2 incorrecta. Trate otra vez")
            self.change_cards()
        else:
            self.player[self.i]._Players__influence1 = list1[answer-1]
            self.player[self.i]._Players__influence2 = list1[answer2-1]
        for i in range(0,4):
            if i != answer and i != answer2:
                self.influences.append(list1[i])
                random.shuffle(self.influences)
     