from claseManejadorFacultades import ManejadorFacultades

from claseFacultad import Facultad

class Menu(object):
    __switcher = None
    __facultades: ManejadorFacultades

    def __init__(self, facultades):
        self.__switcher = { 0:self.salir,
                            1:self.inciso1,
                            2:self.inciso2,
                         }
        self.__facultades = facultades

    def getSwitcher(self):
        return self.__switcher

    def option(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Fin programa')

    def inciso1(self):
        band = False
        while not band:
            try:
                codigo = int(input('Ingrese el código de una Facultad: '))
            except Exception:
                print('Error: se esperaba un entero')
            else:
                self.__facultades.mostrar_nombre_facultad_nombre_y_duracion_carreras(codigo)
                band = True

    def inciso2(self):
        nom_carrera = input('Ingrese el nombre de una Carrera: ')
        self.__facultades.mostrar_codigo_carrera_nombre_y_localidad_facultad(nom_carrera)
