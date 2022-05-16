from claseJugador import Jugador

class ManejadorJugadores(object):
    __jugadores: list

    def __init__(self):
        self.__jugadores = []
    
    def _validar_jugador(self, dato):
        if type(dato) != Jugador:
            raise TypeError('Se espera un Jugador')
    
    def _hay_jugadores(self):
        return len(self.__jugadores) != 0
    
    def agregarJugador(self, jugador):
        self._validar_jugador(jugador)

        self.__jugadores.append(jugador)

    def mostrarJugadores(self):
        for jugador in self.__jugadores:
            print(jugador)

    def buscarJugador(self, dni) -> int:
        retorno = None
        if self._hay_jugadores():
            band = False
            i = 0
            while not band and i < len(self.__jugadores):
                jugador = self.__jugadores[i]
                if jugador.getDni().lower() == dni.lower():
                    retorno = i
                    band = True
                i += 1
        if not band:
            print('Jugador de DNI {} no encontrado...'.format(dni))
        return retorno


    def getJugador(self, indice) -> Jugador:
        return self.__jugadores[indice]