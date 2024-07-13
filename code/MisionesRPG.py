'''
Enunciado "Misiones RPG
Desarrollar un sistema de misiones para un videojuego de rol (RPG) donde se utilicen listas,
sets (conjuntos), tuplas y diccionarios. El sistema debe permitir a los jugadores realizar las 
siguientes acciones

1. Agregar nuevas misiones: El jugador puede aceptar nuevas misiones de NPCs
2. Completar misiones: El jugador puede completar misiones y recibir recompensas. 
3. Consultar el estado de las misiones: El jugador puede revisar el estado de todas las misiones
   aceptadas, organizadas por su estado (pendiente, en progreso y completadas).
4. Consultar recompensas: EL jugador puede consultar las recompensas de las misiones compledas. 

Especificaciones
- Misiones: Implentadas como un diccionario donde las claves son los IDs de las misiones y los valores 
            son tuplas que contienen el nombre de la misión, su descripción, su estado (pendiente, en 
            progreso, completadas) y la recompensas. 
- Estado de las misiones: Implementadas como diccionarios donde las claves son los tipos de recompensas
                          (ejemplo: oro, experiencia, objetos, etc) y los valores son la cantidad correspondientes.
- Recompensas: Implementadas como diccionarios donde las claves son los tipos de recompensas y los valores 
               son las cantidades correspondientes. 
- Inventario del jugador: Actualizado con las recompensas obtenidas al completar las misiones.
'''

# Misiones predefinidas 
misiones = {
    1: ("Rescatar al aldeano", "Rescata al aldeano perdido en el bosque", {"oro": 100, "experiencia": 50}),
    2: ("Recoletar hierbas", "Recolecta 10 hierbas medicinales", {"oro": 50, "experiencia": 30}),
    3: ("Derrota al jefe", "Derrota al jefe de la cueva", {"oro": 200, "experiencia": 100, "objeto": "espada magica"}),
}

# Estado de misiones del jugador
misiones_jugador = {
    "pendientes": set(),
    "progreso": set(),
    "completadas": set()
}

# Inventario del jugador (recompensas)
inventario_jugador = {
    "oro": 0,
    "experiencia": 0,
    "objetos": []
}

def aceptar_mision(id_mision):
    if id_mision in misiones:
        misiones_jugador["pendientes"].add(id_mision)
    else:
        print("ID de misión no valido.")

def comenzar_mision(id_mision):
    if id_mision in misiones_jugador["pendientes"]:
        misiones_jugador["pendientes"].remove(id_mision)
        misiones_jugador["progreso"].add(id_mision)
    else:
        print("La misión no está pendiente o no existe")

def completar_mision(id_mision):
    if id_mision in misiones_jugador["progreso"]:
        misiones_jugador["progreso"].remove(id_mision)
        misiones_jugador["completadas"].add(id_mision)

        recompensas = misiones[id_mision][2]
        for tipo, cantidad in recompensas.items():
            if tipo == "objeto":
                inventario_jugador["objetos"].append(cantidad)
            else:
                inventario_jugador[tipo] += cantidad
    else:
        print("La misión no está en progreso o no existe.")

def consultar_misiones():
    print("Misiones pendientes:")
    for id_mision in misiones_jugador["pendientes"]:
        print(f"{id_mision}: {misiones[id_mision][0]} - {misiones[id_mision][1]}")

    print("\nMisiones en progreso:")
    for id_mision in misiones_jugador["progreso"]:
        print(f"{id_mision}: {misiones[id_mision][0]} - {misiones[id_mision][1]}")

    print("\nMisiones completadas:")
    for id_mision in misiones_jugador["completadas"]:
        print(f"{id_mision}: {misiones[id_mision][0]} - {misiones[id_mision][1]}")

def consultar_recompensas():
    print(f"Oro: {inventario_jugador['oro']}")
    print(f"Experiencia: {inventario_jugador['experiencia']}")
    print(f"Objetos: {', '.join(inventario_jugador['objetos'])}")

# Ejemplo de uso -> UnitTest
aceptar_mision(1)
aceptar_mision(2)
aceptar_mision(3)
consultar_misiones()
comenzar_mision(1)
comenzar_mision(3)
consultar_misiones()
completar_mision(1)
consultar_misiones()
consultar_recompensas()
completar_mision(3)
consultar_misiones()
consultar_recompensas()