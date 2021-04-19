#esta es la clase de la accion ingreso
#SOLO LO VOY A ESCRIBIR ACA PERO ES PARA TODAS LAS ACCIONES
#deberiar recibir a el jugador la ejecuta(parametro i), tambien deberia recibir sus influencias que tiene el jugador,

class Entry:
    #CONSTRUCTOR
    def __init__(self,player,i):
        self.player = player
        self.i = i


    def a_entry(self):
        self.player[self.i]._Players__coins += 1
        return 0
