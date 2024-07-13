import numpy as np
import json
# import funciones
from funciones import *
with open("pacientes.json", "r") as pacientes:
    lista_vieja = json.load(pacientes)


datos_lista = []
# p = paciente
for p in lista_vieja:
    paciente = [p["nombre"], p["rut"], p["edad"], p["sexo"], p["fono"], p["diagnostico"], p["medicamentos"]]
    # print(paciente)
    datos_lista.append(paciente)
# print(datos_lista)
for p in datos_lista:
    # print(p)
    z = 0
    for i in range(0,7):
       if i==0:
           pac[z,i]=p[0]
           print(pac[z,i])
       elif i==1:
           pac[z,i]=p[1]
           print(pac[z,i])
       elif i==2:
           pac[z,i]=p[2]
       elif i==3:
           pac[z,i]=p[3]
       elif i==4:
           pac[z,i]=p[4]
       elif i==5:
           pac[z,i]=p[5]
       elif i==6:
           pac[z,i]=p[6]

    z+=1
# print(pac)
f= len(datos_lista)
while(True):
    showMenu()
    opt=isNum()
    if opt==1:
        for i in range(0,7):
            if i==0:
                pac[f,i]=input("Ingrese el nombre del paciente: ")
            elif i==1:

                pac[f,i]=isRut()
            elif i==2:
                print("Ingrese la edad del paciente")
                pac[f,i]=input()
            elif i==3:
                print("Ingrese el sexo del paciente")
                pac[f,i]=input()
            elif i==4:
                print("Ingrese el fono del paciente")
                pac[f,i]=input()
            elif i==5:
                print("Ingrese el diagnóstico del paciente")
                pac[f,i]=input()
            elif i==6:
                print("Ingrese medicamentos recetados del paciente")
                pac[f,i]=input()
        f+=1
        print("Paciente ingresado con éxito")
    elif opt==2:
        print("Ingrese el rut del paciente a buscar")
        x=input()
        for i in range(0,50):
            if x==pac[i,1]:
                print("Paciente encontrado, sus datos son los siguientes:")
                for j in range(0,6):
                    showPatient(i,j)

                break
        else:
            print("Paciente no encontrado")
    elif opt==3:
        print("Ingrese el rut del paciente a buscar")
        x=input()
        for i in range(0,50):
            if x==pac[i,1]:
                print("Paciente encontrado, los medicamentos recetados son los siguientes:")
                print(pac[i,6])
                break
        else:
            print("Paciente no encontrado")
    elif opt==4:
        print("Ingrese el rut del paciente a eliminar")
        x=input()
        for i in range(0,50):
            if x==pac[i,1]:
                pac=np.delete(pac,i, axis=0)
                print("Paciente eliminado con éxito")
                break
        else:
            print("Paciente no encontrado")
    elif opt==5:
        for i in range(0, len(datos_lista) ):
            print("Paciente:")
            for j in range(0,6):
                showPatient(i,j)
    elif opt==6:
        # Creo una lista para quitar los NONES
        lista_pacientes = []
        # Recorro la matriz para validar
        for p in pac:

          if p[0] == None:

            break
          else:
            # Agrego a la nueva matriz los datos
            lista_pacientes.append(p)

        lista_nueva = []
        for p in lista_pacientes:

          diccionario_paciente = {
            "nombre": p[0],
            "rut": p[1],
            "edad" : p[2],
            "sexo" : p[3],
            "fono" : p[4],
            "diagnostico" : p[5],
            "medicamentos" : p[6]
          }
          lista_vieja.append(diccionario_paciente)



        with open ("pacientes.json", "w") as pacientes:
            json.dump(lista_vieja, pacientes)
            print("Datos ingresados al archivo pacientes.json")






        # print(lista_pacientes)



        break
    else:
        print("Error, ingrese opción válida")