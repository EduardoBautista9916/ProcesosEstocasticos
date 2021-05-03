from os import system

def main():
    print("Ingrese el Número de estados")
    num_estados = val_numI()
    estados = []
    for i in range(0,num_estados):
        system("cls")
        aux = []
        print("Salidas del Nodo", i, "\n------------------------------------------------------------")
        for j in range(0,num_estados):
            print("Ingrese el valor de salida al nodo", j , ":")
            aux.append(val_numF())
        estados.append(aux)
    system("cls")
    print("Potencia (Numero de pasos)")
    potencia=val_numI()
    print("Mostrar detalle s/n")
    detalle=val_S_N()
    matEstado=estados
    if(detalle=="s"):
        system("cls")
        print("Matriz Inicial")
        imprimir(estados)
        system("pause")
    for i in range(0,potencia-1):
        matEstado=mul_mat(estados,matEstado)
        if(detalle=="s" or i == potencia-2):
            system("cls")
            print("Matriz de Paso",i+2)
            imprimir(matEstado)
            system("pause")


def mul_mat(matA,matB):
    matC = []
    for i in range(0,len(matA)):
        aux=[]
        for j in range(0,len(matB)):
            suma=0
            for k in range(0, len(matA)):
                suma += matA[i][k]*matB[k][j]
            aux.append(suma)
        matC.append(aux)
    return matC


def val_numI():
    try:
        digit= int(input(">"))
    except(ValueError):
        print("VALOR NO VALIDO")
        digit=val_num()
    return digit

def val_numF():
    try:
        digit= float(input(">"))
    except(ValueError):
        print("VALOR NO VALIDO")
        digit=val_num()
    return digit

def val_S_N():
    val=input()
    if(val=="s" or val=="n"):
        return val
    else:
        print("Opcion no Valida")
        val=val_S_N()

def imprimir(mat):
    for i in range(0,len(mat)):
        for j in range(0,len(mat)):
            print(mat[i][j], "  ",end="")
        print()

main()