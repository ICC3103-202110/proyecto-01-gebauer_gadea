#esta es la clase de la accion ingreso
#SOLO LO VOY A ESCRIBIR ACA PERO ES PARA TODAS LAS ACCIONES
#deberiar recibir a el jugador la ejecuta(parametro i), tambien deberia recibir sus influencias que tiene el jugador,
from actions import Actions
class Entry(Actions):
    #CONSTRUCTOR
    def __init__(self,player,i):
        super(Entry, self).__init__(player,i)

    #METODOS
    def change_coins(self):
        self.player[self.i]._Players__coins += 1

    def a_entry(self):
        self.change_coins()
        return 0
