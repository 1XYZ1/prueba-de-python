import numpy as np
pac=np.empty([50,7],dtype="object")



def isNum():
    while(True):
            op = input('Ingrese una opción: ')
            if op.isdigit():
                op = int(op)
                return(op)
            else:
                print("Error, se esperaba un número, reintente")


def showMenu():
    print("SERVICIO DE ATENCIÓN MÉDICA DE URGENCIAS")
    print("----------------------------------------")
    print("1) Ingresar Ficha del Paciente")
    print("2) Buscar Ficha por Rut")
    print("3) Buscar Medicamentos por Rut")
    print("4) Eliminar Ficha del Paciente")
    print("5) Listar Pacientes Atendidos")
    print("6) Salir")
def isRut():
    while(True):
        x=input("Ingrese el rut del paciente: ")
        if x=="":
            print("Error, campo ingresado vacío, reintente")
        else:
            break
    return(x)

def showPatient(i,j):
    if j==0:
        print("Nombre:",pac[i,j])
    elif j==1:
        print("Rut:",pac[i,j])
    elif j==2:
        print("Edad:",pac[i,j])
    elif j==3:
        print("Sexo:",pac[i,j])
    elif j==4:
        print("Fono:",pac[i,j])
    elif j==5:
        print("Diagnóstico:")
        print(pac[i,j])