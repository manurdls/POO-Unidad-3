import csv

from claseManejadorFlores import ManejadorFlores

from claseFlor import Flor

from claseManejadorRamos import ManejadorRamos

from claseMenu import Menu

def cargar_datos_flores() -> ManejadorFlores:
    flores = ManejadorFlores()
    archivo = open('flores.csv')
    reader = csv.reader(archivo, delimiter=';')
    for linea in reader:
        flores.agregarFlor(Flor(int(linea[0]), linea[1], linea[2], linea[3]))
    archivo.close()
    return flores


def menu(flores, ramos):
    menu = Menu(flores, ramos)
    exit = False
    while not exit:
        print("---------------MENU---------------\n"
              "1.Registrar un ramo vendido (instancia de la clase ramo), solicitando las flores que se pondrán en el ramo\n"
              "2.Mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos\n"
              "3.Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos\n"
              "0.Salir")
        opt = int(input('Ingrese una opcion: '))
        menu.option(opt)
        exit = opt==0

if __name__ == '__main__':
    flores = cargar_datos_flores()
    ramos = ManejadorRamos()
    menu(flores, ramos)