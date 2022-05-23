from claseCalefactor import Calefactor

class CalefactorGas(Calefactor):
    __matricula: str
    __calorias: int

    def __init__(self, matricula, calorias, marca, modelo):
        #Validación

        self.__matricula = matricula
        self.__calorias = calorias
        super().__init__(marca, modelo)

    def getMatricula(self):
        return self.__matricula

    def getCalorias(self):
        return self.__calorias

    def __str__(self):
        retorno = super().__str__()
        retorno += "Matricula: {} Calorias: {}".format(self.__matricula, self.__calorias)
        return retorno