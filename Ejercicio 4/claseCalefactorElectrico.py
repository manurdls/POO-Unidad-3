from claseCalefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __potencia_maxima: int

    def __init__(self, potencia_maxima, marca, modelo):
        #Validación

        self.__potencia_maxima = potencia_maxima
        super().__init__(marca, modelo)

    def getPotenciaMaxima(self):
        return self.__potencia_maxima

    def __str__(self):
        retorno = super().__str__()
        retorno += 'Potencia Maxima: {}'.format(self.__potencia_maxima)
        return retorno