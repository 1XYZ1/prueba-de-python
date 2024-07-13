import json
import numpy as np
# Abrir pacientes, r es permiso de lectura
matrix = np.empty(50, dtype=object)
with open('matrix/pacientes2.json', 'r') as pacientes:
    datos = json.load(pacientes)

#Este for es para convertir datos en una lista de listas
datos_lista = []
# p = paciente
for p in datos:
    paciente = [p["nombre"], p["apellido"], p["rut"], p["edad"], p["peso"], p["sexo"], p["telefono"], p["diagnostico"], p["medicamentos"]]
    # print(paciente)
    datos_lista.append(paciente)

# print(datos_lista)
#Se convierte la lista de listas en una matriz bidimensional (Medicamentos tri-dimensional)
matrix = np.array(datos_lista, dtype=object)

# print(matrix[0][5])
#Mi primer intento de convertir datos en una matriz
'''
for i in range(len(datos)):
    datos[i][0] = datos[i].pop("nombre")
    datos[i][1] = datos[i].pop("apellido")
    datos[i][2] = datos[i].pop("rut")
    datos[i][3] = datos[i].pop("edad")
    datos[i][4] = datos[i].pop("peso")
    datos[i][5] = datos[i].pop("medicamentos")

    # print(datos[i])
    # matrix[i] = datos[i]
matrix = np.array(datos)
# print(matrix[0][0]) '''

def agregar_paciente():

    nuevo_paciente = pedir_datos('paciente') # Retorna un diccionario con los datos del paciente
    # convertir el diccionario en una lista
    datos_pacientes = []
    for i in nuevo_paciente:
        datos_pacientes.append(nuevo_paciente[i])
    #data = p["nombre"], p["apellido"], p["rut"], p["edad"], p["peso"], p["medicamentos"]
    #datos_pacientes.append(data)
    #print(datos_pacientes)

    #agregar paciente a la lista de pacientes y a la matriz
    datos_lista.append(datos_pacientes)

    #Se convierte la lista de listas en una matriz bidimensional (Medicamentos tri-dimensional)
    global matrix     # Importar variable global matrix para acceder fuera de la funcion
    global datos     # Importar variable global datos para acceder fuera de la funcion
    matrix = np.array(datos_lista, dtype=object)

    #agregar a datos para guardar en el archivo
    datos.append(nuevo_paciente)
    print(f'Paciente {nuevo_paciente["nombre"].capitalize()} {nuevo_paciente["apellido"].capitalize()} agregado con exito.')
    # print(matrix)

    #Guardar la lista en el archivo pacientes
    # with open('matrix/pacientes2.json', 'w') as pacientes:
    #     json.dump(datos, pacientes)

def buscar_paciente(metodo_busca='rut'):

    rut = input('Ingrese el rut del paciente: ')
    #buscar paciente por rut
    if(metodo_busca == 'rut'):
        for i in range(len(matrix)):
            if rut == matrix[i][2]:
                print('\nDatos del paciente: ')
                print(f'Nombre: {matrix[i][0].capitalize()}')
                print(f'Apellido: {matrix[i][1].capitalize()}')
                print(f'Rut: {matrix[i][2]}')
                print(f'Edad: {matrix[i][3]}')
                print(f'Peso: {matrix[i][4]}')
                print(f'Sexo: {matrix[i][5]}')
                print(f'Telefono: {matrix[i][6]}')
                print(f'Diagnostico: {matrix[i][7]}\n')
                break
        else:
            print('Paciente no encontrado')

    if(metodo_busca == 'med'):
        for i in range(len(matrix)):
            if rut == matrix[i][2]:
                print(f'Medicamentos del paciente {matrix[i][0].capitalize()} {matrix[i][1].capitalize()}:')

                for indice, med in enumerate(matrix[i][8], start=1):
                    print(f'{indice}) {med.capitalize()}')

def eliminar_paciente():
    global matrix     # Importar variable global matrix para acceder fuera de la funcion
    global datos     # Importar variable global datos para acceder fuera de la funcion
    rut = input('Ingrese el rut del paciente: ')
    continuar = input('Esta seguro que desea eliminar al paciente? si/no: ').lower().strip()

    # validar si el usuario desea eliminar al paciente
    if continuar == 'no':
        print('Operacion cancelada')
        return

    for i in range(len(matrix)):
        if rut == matrix[i][2]:
            matrix = np.delete(matrix, i, axis=0)

            #Metodo largo, se debe convertir la matriz en json
            for p in (matrix):
                paciente = {
                "nombre": p[0],
                "apellido": p[1],
                "rut": p[2],
                "edad": p[3],
                "peso": p[4],
                "sexo": p[5],
                "telefono": p[6],
                "diagnostico": p[7],
                "medicamentos": p[8]
                }
                datos.append(paciente)

            #Guardar la lista actualizada (paciente eliminado) en el archivo pacientes

            # with open('matrix/pacientes2.json', 'w') as pacientes:
            #     json.dump(nuevos_datos, pacientes)
            # print(nuevos_datos)

            #Eliminar paciente de la lista de pacientes
            #datos.pop(i) Easy method
            #Guardar la lista en el archivo pacientes
            #with open('matrix/pacientes2.json', 'w') as pacientes:
            #    json.dump(datos, pacientes)

            print('\nPaciente eliminado con exito')
            break
    else:
        print('Paciente no encontrado')

def listar_pacientes():
    for i in range(len(matrix)):
        print(f'\n {i + 1}) {matrix[i][0].capitalize()} {matrix[i][1].capitalize()} {matrix[i][2]}')


def guardar_datos():

    with open('matrix/pacientes2.json', 'w') as pacientes:
                json.dump(datos, pacientes)

# Esta funcion pide los datos de una persona y retorna un diccionario ("pacientes") para pedir medicamentos y diagnosticos
# Podriamos pedir datos de un medico o cualquier otra persona
def pedir_datos(persona: str = ''):
    # pedir datos del paciente
    try:
        nombre = str(input(f'Ingrese el nombre: '))
    except:
        print('')
    apellido = input(f'Ingrese el apellido: ')
    rut = input(f'Ingrese el rut: ')
    edad = input(f'Ingrese la edad: ')
    peso = input(f'Ingrese el peso: ')
    sexo = input(f'Ingrese el sexo: ')
    telefono = input(f'Ingrese el telefono: ')
    diagnostico = input(f'Ingrese el diagnostico: ')


    if persona == "paciente":
        # Logica medicamentos (Se agrega un medicamento a la lista de medicamentos)
        med = input('Desea ingresar medicamentos? si/no: ').lower().strip()
        medicamentos = []
        if med == 'si':
            while True:
                medicamento = input('Ingrese el medicamento: ')
                medicamentos.append(medicamento)
                med = input('Desea ingresar otro medicamento? si/no: ').lower().strip()
                if med == 'no':
                    break
    # agregar los datos obtenidos en un diccionario
    diccionario = {
    'nombre' : nombre,
    'apellido' : apellido,
    'rut' : rut,
    'edad' : edad,
    'peso' : peso,
    'sexo' : sexo,
    'telefono' : telefono,
    'diagnostico' : diagnostico,
    }
    # Si la persona es un paciente, se agrega la lista de medicamentos al diccionario
    if persona == "paciente":
        diccionario['medicamentos'] = medicamentos

    return diccionario

# eliminar_paciente()
# buscar_paciente('rut')
# agregar_paciente()
# listar_pacientes()