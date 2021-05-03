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
    print("Estado Inicial")
    x=val_numI()
    print("Estado Final")
    y=val_numI()
    print("Numero de Periodos (Numero de pasos)")
    potencia=val_numI()
    mat_pot=[]
    prim_Vez=[]
    mat_Ciclo=[]
    mat_pot.append(estados[x][y])
    prim_Vez.append(estados[x][y])
    mat_Ciclo.append(estados[y][y])
    print("Mostrar detalle s/n")
    detalle=val_S_N()
    matEstado=estados
    if(detalle=="s"):
        system("cls")
        print("Paso Inicial")
        imprimir(estados)
        print()
        print("P(T=1)= ",prim_Vez[0])
        
        system("pause")
    for i in range(1,potencia):
        matEstado=mul_mat(estados,matEstado)
        mat_pot.append(matEstado[x][y])
        mat_Ciclo.append(matEstado[y][y])
        suma=0
        cadena=""
        cadena+="P(T="+str(i+1)+")=" + str(matEstado[x][y])+"-["
        for j in range(0,i):
            suma += prim_Vez[j]*mat_Ciclo[i-j-1]
            cadena+="("+str(prim_Vez[j])+")("+str(mat_Ciclo[i-j-1])+")"
            if(j!=i-1):
                cadena+="+"
        prim_Vez.append(matEstado[x][y]-suma)
        if(detalle=="s" or i == potencia-1):
            system("cls")
            print("Paso",i+1)
            print()
            cadena+="]="+str(prim_Vez[i])
            print(cadena)
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