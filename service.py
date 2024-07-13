import random
import json

# valores = [1,3,4]
# dato = statistics.geometric_mean(valores)
# print(dato)

# Variables gloabales
trabajadores = ["Juan Perez", "María García", "Carlos López", "Ana Martinez", "Pedro Rodriguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
lista_trabajadores = []

def isNum():
    while(True):
            op = input('Ingrese una opción: ')
            if op.isdigit():
                op = int(op)
                return(op)
            else:
                print("Error, se esperaba un número, reintente")

def Asignar_sueldos():

    global lista_trabajadores
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        dic = {"nombre": trabajador, "sueldo": sueldo}
        lista_trabajadores.append(dic)


        # print(dic)
    # aleatorio = random.randint(300000, 2500000)
    # print(lista_trabajadores)
    print("Sueldos asignado con exito")
# Asignar_sueldos()

def Clasificar_sueldos():
    rango1 = [0]
    rango2 = [0]
    rango3 = [0]
    total = 0

    for i in lista_trabajadores:
        if i["sueldo"] < 800:
            rango1[0] +=1
            total = total + i["sueldo"]
            rango1.append(i)

        if i["sueldo"] >= 800 and i["sueldo"] <= 2000:
            rango2[0] +=1
            total = total + i["sueldo"]
            rango2.append(i)

        if i["sueldo"] > 2000:
            rango3[0] +=1
            total = total + i["sueldo"]
            rango3.append(i)

    if len(lista_trabajadores) > 0:
        # Primer Rango
        print(f"Sueldos menores a $800.000 TOTAL: {rango1[0]}\n")
        print("Nombre Empleado     Sueldo")
        for i in range(1, len(rango1)):

            print(f"{rango1[i]["nombre"]}     ${rango1[i]["sueldo"]}")
        # Segundo Rango
        print(f"\nSueldos entre a $800.000 y $2.000.000 TOTAL: {rango2[0]}\n")
        print("Nombre Empleado     Sueldo")
        for i in range(1, len(rango2)):

            print(f"{rango2[i]["nombre"]}     ${rango2[i]["sueldo"]}")
        # Tercer Rango
        print(f"\nSueldos superiores a $2.000.000 TOTAL: {rango3[0]}\n")
        print("Nombre Empleado     Sueldo")
        for i in range(1, len(rango3)):

            print(f"{rango3[i]["nombre"]}     ${rango3[i]["sueldo"]}")
        print(f"TOTAL SUELDOS: {total}" )
    else:
         print("Debe asignar sueldo a los trabajadores")

def ver_estadisticas():


    alto = 0
    bajo = 2500000
    total = 0
    for i in lista_trabajadores:
        if i["sueldo"] > alto:
            alto = i["sueldo"]

    for i in lista_trabajadores:
        if i["sueldo"] < bajo:
            bajo = i["sueldo"]
    for i in lista_trabajadores:
        total += i["sueldo"]


    print(f"El sueldo más alto es: {alto}")
    print(f"El sueldo más bajo es: {bajo}")
    print(f"El sueldo promedio es: {total / len(lista_trabajadores)}")
    # PENDIENTE MEDIA GEOMETRICA
# ver_estadisticas()
# Clasificar_sueldos()

def reporte_sueldos():
    reporte_json = []
    print("Nombre empleado  Sueldo Base  Descuento Salud  Descuento AFP  Sueldo Líquido")
    for i in lista_trabajadores:

        descuento_salud = i["sueldo"] * 0.07
        descuento_afp = i["sueldo"] * 0.12
        sueldo_liquido = i["sueldo"] - descuento_salud - descuento_afp
        print(f"{i["nombre"]}    ${i["sueldo"]}    ${descuento_salud}    ${descuento_afp}     ${ sueldo_liquido}")

        trabajador = {
            "nombre": i["nombre"],
            "sueldo_base":i["sueldo"],
            "descuento_salud": descuento_salud,
            "descuento_afp": descuento_afp,
            "sueldo_liquido": sueldo_liquido
        }
        reporte_json.append(trabajador)
    with open('reporte.json', 'w') as data:
        json.dump(reporte_json, data)
# reporte_sueldos()
