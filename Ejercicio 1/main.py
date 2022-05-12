import csv

from claseFacultad import Facultad

from claseMenu import Menu

from claseManejadorFacultades import ManejadorFacultades

def leer_datos():
    facultades = ManejadorFacultades()
    archivo = open('Facultades.csv')
    reader = csv.reader( archivo, delimiter = ';' )
    filaFacultad=next(reader)
    bandera = True
    while bandera:
        facultad = Facultad(int(filaFacultad[0]), filaFacultad[1], filaFacultad[2], filaFacultad[3], filaFacultad[4])
        facultades.agregarFacultad(facultad)
        filaCarrera=next(reader)
        while bandera and filaFacultad[0]==filaCarrera[0]:
            facultad.agregarCarrera(int(filaCarrera[1]), filaCarrera[2], filaCarrera[3], filaCarrera[4], filaCarrera[5])
            try:
                filaCarrera=next(reader)
            except StopIteration:
                bandera=False
        filaFacultad=filaCarrera
    archivo.close()
    return facultades

def menu(facultades):
    menu = Menu(facultades)
    exit = False
    while not exit:
        print("---------------MENU---------------\n"
              "1.Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.\n"
              "2.Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.\n"
              "0.Salir")
        opt = int(input('Ingrese una opcion: '))
        menu.option(opt)
        exit = opt==0



if __name__ == '__main__':
    facultades = leer_datos()
    menu(facultades)