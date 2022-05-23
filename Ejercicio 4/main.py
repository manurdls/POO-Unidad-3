import os

from claseMenu import Menu

from claseManejadorCalefactores import ManejadorCalefactores

from claseCalefactorElectrico import CalefactorElectrico

from claseCalefactorGas import CalefactorGas

def test():
    calGas = CalefactorGas("ASDF-ASDF", 500, "MarcaGas", "ModeloGas")
    calElectrico = CalefactorElectrico(1000, "MarcaElectrico", "ModeloElectrico")
    print(calGas)
    print(calElectrico)

def cargar_datos_calefactores_electricos():
    pass

def cargar_datos_calefactores_a_gas():
    pass

def menu(calefactores):
    os.system('cls')
    menu = Menu(calefactores)
    exit = False
    while not exit:
        print("----------------------MENU----------------------\n"
              "1.Iniciar funcionalidad\n"
              "0.Salir")
        opt = input('Ingrese una opcion: ')
        os.system('cls')
        print('---------------------------------------------------------------------------------------------')
        print("***IMPORTANTE*** USTED PUEDE CANCELAR LA OPERACION EN CUALQUIER MOMENTO SI INGRESA 'cancelar'")
        print('---------------------------------------------------------------------------------------------')
        if opt.lower() == 'cancelar':
            opt = 0
        else:
            opt = int(opt)
        menu.option(opt)
        exit = opt==0

if __name__ == "__main__":
    #test()
    tamanio = int(input("Ingrese el tamanio del arreglo: "))
    calefactores = ManejadorCalefactores(tamanio)
    cargar_datos_calefactores_electricos(calefactores)
    cargar_datos_calefactores_a_gas(calefactores)
    menu(calefactores)