from claseFacultad import Facultad

class ManejadorFacultades(object):

    __facultades: list

    def __init__(self):
    
        self.__facultades = []

    def agregarFacultad(self, facultad):
        if type(facultad) != Facultad:
            raise TypeError('Se espera una facultad')
        self.__facultades.append(facultad)

    def _buscar_facultad_por_codigo(self, codigo):
        retorno = None
        band = False
        i = 0
        cant_facultades = len(self.__facultades)
        while not band and i < cant_facultades:
            if self.__facultades[i].getCodigo() == codigo:
                band = True
                retorno = i
            i += 1
        if band == False:
            print("No se encontró una Facultad cuyo código sea: {}".format(codigo))
        return retorno

    def _obtener_carrera_y_facultad_por_nombre_de_carrera(self, nom_carrera):
        carrera = None
        facultad = None
        i = 0
        band = False
        cant_facultades = len(self.__facultades)
        while not band and i < cant_facultades:
            carrera = self.__facultades[i].obtener_carrera_por_nombre(nom_carrera)
            if carrera != None:
                facultad = self.__facultades[i]
                band = True
            i += 1
        if carrera == None: print("No se encontró una Carrera cuyo nombre sea: {}".format(nom_carrera))
        return (carrera, facultad)

    def mostrar_nombre_facultad_nombre_y_duracion_carreras(self, codigo):
        indice_facultad = self._buscar_facultad_por_codigo(codigo)
        if indice_facultad != None:
            print('Nombre Facultad: {}'.format(self.__facultades[indice_facultad].getNombre()))
            print('Carreras:')
            self.__facultades[indice_facultad].mostrar_nombre_y_duracion_carreras()

    def mostrar_codigo_carrera_nombre_y_localidad_facultad(self, nom_carrera):
        carrera_y_facultad = self._obtener_carrera_y_facultad_por_nombre_de_carrera(nom_carrera)
        carrera = carrera_y_facultad[0]
        facultad = carrera_y_facultad[1]
        
        # Nota: la generación del código de la carrera se podría optimizar para que sea único.
        # La solución propuesta es a modo práctico
        if (carrera != None) and (facultad != None):
            print('Codigo de la carrera: {}{}\nNombre de la facultad donde se dicta: {}\nLocalidad de la facultad donde se dicta: {}'.format(facultad.getCodigo(),
                                                                                                                                             carrera.getCodigo(),
                                                                                                                                             facultad.getNombre(),
                                                                                                                                             facultad.getDepartamento()))