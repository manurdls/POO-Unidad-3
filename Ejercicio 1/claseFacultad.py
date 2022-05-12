from claseCarrera import Carrera

from claseManejadorCarreras import ManejadorCarreras

class Facultad(object):
    __codigo: int
    __nombre: str
    __direccion: str
    __departamento: str
    __telefonos: str
    __carreras: ManejadorCarreras

    def __init__(self, cod, nom, dir, dep, tel):
        
        # Una forma de validar los datos
        self._validar_entero(cod)
        self._validar_cadena(nom)
        self._validar_cadena(dir)
        self._validar_cadena(dep)
        self._validar_cadena(tel)
    
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = dir
        self.__departamento = dep
        self.__telefonos = tel
        self.__carreras = ManejadorCarreras()

    def _validar_entero(self, dato):
        if type(dato) != int:
            raise TypeError('Se espera una cadena')

    def _validar_cadena(self, dato):
        if type(dato) != str:
            raise TypeError('Se espera una cadena')
        

    def __str__(self):
        return 'Código: {}, Nombre: {}'.format(self.__codigo, self.__nombre)

    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre

    def getDepartamento(self):
        return self.__departamento

    def getCantCarreras(self):
        return self.__carreras.getCantidadCarreras()

    def agregarCarrera(self, cod, nom, titulo, cant_sem, tipo_tit):
        self.__carreras.agregarCarrera(Carrera(cod, nom, titulo, cant_sem, tipo_tit))

    def mostrar_nombre_y_duracion_carreras(self):
        self.__carreras.mostrar_nombre_y_duracion_carreras()

    def obtener_carrera_por_nombre(self, nom_carrera):
        return self.__carreras.obtener_carrera_por_nombre(nom_carrera)