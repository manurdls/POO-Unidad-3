

class Calefactor(object):
    __marca: str
    __modelo: str

    def __init__(self, marca, modelo):
        #Validaciones

        self.__marca = marca
        self.__modelo = modelo

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def __str__(self):
        return "Marca: {} Modelo: {}".format(self.__marca, self.__modelo)