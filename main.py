from service import *


trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

while True:
    print('1. Asignar sueldos aleatorios')
    print('2. Clasificar sueldos')
    print('3. Ver estadísticas')
    print('4. Reporte de sueldos')
    print('5. Salir del programa')
    op = isNum()

    match op:
        case 1:
            Asignar_sueldos()
        case 2:
            Clasificar_sueldos()
        case 3:
            ver_estadisticas()
        case 4:
            reporte_sueldos()
        case 5:
            print("Finalizando programa...")
            print("Desarrollado por Ramon Hernandez ^^")
            print("RUT 26.234.362-6")
            break