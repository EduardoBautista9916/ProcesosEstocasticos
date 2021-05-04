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
    """estados=[[0.917,0.051,0.011,0.001,0.020],[0.511,0.300,0.056,0.039,0.94],[0.019,0.146,0.427,0.297,0.112],[0.008,0.050,0.295,0.511,0.136],[0,0,0,0,1]]"""
    while(True):
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
            imprimir(estados)
            print("Paso Inicial")
            imprimir(estados)
            print()
            print("P(T=1)= ","{0:0.4f}".format(prim_Vez[0]))
            
            system("pause")
        for i in range(1,potencia):
            matEstado=mul_mat(estados,matEstado)
            mat_pot.append(matEstado[x][y])
            mat_Ciclo.append(matEstado[y][y])
            suma=0
            cadena=""
            cadena+="P(T="+str(i+1)+")=" + "{0:0.4f}".format(matEstado[x][y])+"-["
            for j in range(0,i):
                suma += prim_Vez[j]*mat_Ciclo[i-j-1]
                cadena+="("+"{0:0.4f}".format(prim_Vez[j])+")("+"{0:0.4f}".format(mat_Ciclo[i-j-1])+")"
                if(j!=i-1):
                    cadena+="+"
            prim_Vez.append(matEstado[x][y]-suma)
            if(detalle=="s" or i == potencia-1):
                system("cls")
                imprimir(matEstado)
                print("Paso",i+1)
                print()
                cadena+="]="+"{0:0.4f}".format(prim_Vez[i])
                print(cadena)
                system("pause")
        print("otra vez?")
        opcion=val_S_N()
        if(opcion=="n"):
            break
    
    


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
        return val_S_N()

def imprimir(mat):
    for i in range(0,len(mat)):
        for j in range(0,len(mat)):
            print("{0:0.4f}".format(mat[i][j]), "  ",end="")
        print()

main()