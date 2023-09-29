from Tv import Tv
from Consola import Consola
from Bicicleta import Bicicleta
from Scooter import Scooter

listatvs = []
listaconsolas = []
listascooters = []
listabicicletas = []

def menu():
    while True:
        print("\nMenú Principal:")
        print("1. Registrar TV")
        print("2. Registrar Consola")
        print("3. Registrar Scooter")
        print("4. Registrar Bicicleta")
        print("5. Cotizar TV")
        print("6. Cotizar Consola")
        print("7. Cotizar Scooter")
        print("8. Cotizar Bicicleta")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrartv()
        elif opcion == "2":
            registrarconsola()
        elif opcion == "3":
            registrarscooter()
        elif opcion == "4":
            registrarbicicleta()
        elif opcion == "5":
            cotizartvs()
        elif opcion == "6":
            cotizarconsolas()
        elif opcion == "7":
            cotizarscooters()
        elif opcion == "8":
            cotizarbicicletas()
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def validar_precio():
    while True:
        try:
            precio = int(input("Ingrese precio: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
            else:
                return precio 
        except ValueError:
            print("Debe ingresar un número válido para el precio y mayor que cero.")

def validar_tamano_pulgadas():
    while True:
        try:
            tamano = float(input("Ingrese tamaño (pulgadas): "))
            if tamano <= 0:
                print("El tamaño en pulgadas debe ser mayor que cero.")
            else:
                return tamano  
        except ValueError:
            print("Debe ingresar un número válido para el tamaño en pulgadas y mayor que cero.")

def validar_eficiencia():
    while True:
        eficiencia = input("Ingrese eficiencia (A-F): ").upper()
        if eficiencia not in ['A', 'B', 'C', 'D', 'E', 'F']:
            print("Eficiencia no válida. Ingrese una eficiencia válida (A-F).")
        else:
            return eficiencia

def validar_version_consola():
    while True:
        version = input("Ingrese versión (Normal/Lite): ").capitalize()
        if version not in ['Normal', 'Lite']:
            print("Versión no válida. Ingrese 'Normal' o 'Lite'.")
        else:
            return version

def validar_aro_scooter():
    while True:
        try:
            aro = float(input("Ingrese tamaño del aro: "))
            if aro <= 0:
                print("El tamaño del aro debe ser mayor que cero.")
            else:
                return aro 
        except ValueError:
            print("Debe ingresar un número válido para el tamaño del aro y mayor que cero.")

def validar_velocidad_scooter():
    while True:
        try:
            velocidad = int(input("Ingrese velocidad máxima (km/h): "))
            if velocidad <= 0:
                print("La velocidad máxima debe ser mayor que cero.")
            else:
                return velocidad 
        except ValueError:
            print("Debe ingresar un número válido para la velocidad máxima y mayor que cero.")

def validar_peso_scooter():
    while True:
        try:
            peso = float(input("Ingrese peso (kg): "))
            if peso <= 0:
                print("El peso debe ser mayor que cero.")
            else:
                return peso  
        except ValueError:
            print("Debe ingresar un número válido para el peso y mayor que cero.")

def registrartv():
    marca = input("Ingrese marca de la TV: ")
    while True:
        try:
            voltaje = int(input("Ingrese voltaje: "))
            break  
        except ValueError:
            print("Debe ingresar un número válido para el voltaje.")
    eficiencia = validar_eficiencia()
    tamano = validar_tamano_pulgadas()
    precio = validar_precio()
    tv = Tv(marca, voltaje, eficiencia, precio, tamano)
    listatvs.append(tv)
    print("TV registrada con éxito!")

def registrarconsola():
    nombre = input("Ingrese nombre de la consola: ")
    version = validar_version_consola()
    marca = input("Ingrese marca: ")
    while True:
        try:
            voltaje = int(input("Ingrese voltaje: "))
            break  
        except ValueError:
            print("Debe ingresar un número válido para el voltaje.")
    eficiencia = validar_eficiencia()
    precio = validar_precio()
    consola = Consola(nombre, version, marca, voltaje, eficiencia, precio)
    listaconsolas.append(consola)
    print("Consola registrada con éxito!")

def registrarscooter():
    marca = input("Ingrese marca del scooter: ")
    while True:
        try:
            voltaje = int(input("Ingrese voltaje: "))
            break 
        except ValueError:
            print("Debe ingresar un número válido para el voltaje.")
    eficiencia = validar_eficiencia()
    aro = validar_aro_scooter()
    velocidad = validar_velocidad_scooter()
    peso = validar_peso_scooter()
    precio = validar_precio()
    scooter = Scooter(marca, voltaje, eficiencia, precio, aro, velocidad, peso)
    listascooters.append(scooter)
    print("Scooter registrado con éxito!")

def registrarbicicleta():
    aro = validar_tamano_pulgadas()
    peso = float(input("Ingrese peso (kg): "))
    precio = validar_precio()
    marca = input("Ingrese marca: ")
    bicicleta = Bicicleta(aro, peso, precio, marca)
    listabicicletas.append(bicicleta)
    print("Bicicleta registrada con éxito!")

def cotizartvs():
    for tv in listatvs:
        tv.mostrarInfo()

def cotizarconsolas():
    for consola in listaconsolas:
        consola.mostrarInfo()

def cotizarscooters():
    for scooter in listascooters:
        scooter.mostrarInfo()

def cotizarbicicletas():
    for bicicleta in listabicicletas:
        bicicleta.mostrarInfo()

if __name__ == "__main__":
    menu()
