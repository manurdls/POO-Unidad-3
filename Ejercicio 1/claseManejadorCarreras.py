from claseCarrera import Carrera

class ManejadorCarreras(object):

    __carreras: list

    def __init__(self):
    
        self.__carreras = []

    def _buscar_carrera_por_nombre(self, nom_carrera):
        retorno = None
        band = False
        i = 0
        cant_carreras = len(self.__carreras)
        while not band and i < cant_carreras:
            if self.__carreras[i].validarNombre(nom_carrera):
                band = True
                retorno = i
            i += 1
        #if band == False:
        #    print("No se encontró una Carrera cuyo nombre sea: {}".format(nom_carrera))
        return retorno

    def agregarCarrera(self, carrera):
        if type(carrera) != Carrera:
            raise TypeError('Se espera una carrera')
        self.__carreras.append(carrera)

    def getCantCarreras(self):
        return len(self.__carreras)

    def mostrar_nombre_y_duracion_carreras(self):
        for carrera in self.__carreras:
            print('{}. Duración: {}'.format(carrera.getNombre(), carrera.getCantSemestres()))

    def obtener_carrera_por_nombre(self, nom_carrera):
        retorno = None
        indice_carrera = self._buscar_carrera_por_nombre(nom_carrera)
        if indice_carrera != None:
            retorno = self.__carreras[indice_carrera]
        return retorno
        