from os import system
from PyQt5.QtWidgets import QMessageBox

def main(ui):
    matA=val_numI(ui)
    matAn=[]
    mat_pot=[]
    prim_Vez=[]
    mat_Ciclo=[]
    x=val_numIn(ui,ui.txtyInitial.text(),0)
    y=val_numIn(ui,ui.txtFinal.text(),1)
    potencia=val_numIn(ui,ui.txtNoSteps.text(),2)
    if(matA[0]=="ERROR" or x=="ERROR" or y =="ERROR" or potencia=="ERROR"):
        print("hubo un error al llenar")
        return
    if(x<0 or x>ui.matN-1):
        error(ui,0)
        return
    elif(y<0 or y>ui.matN-1):
        error(ui,1)
        return
    elif(potencia<0):
        error(ui,2)
        return


    """
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
        """
    
    


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


def val_numI(ui):
    try:
        matA=[]
        for i in range(ui.matN):
            aux=[]
            for j in range(ui.matN):
                num=int(ui.tblMatA.item(i,j).text())
                aux.append(num)
            matA.append(aux)
        return matA
    except(ValueError):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Alguno(s) de los Valores de la Matriz no es Valido")
        msgBox.setWindowTitle("ERROR")
        msgBox.setStandardButtons(QMessageBox.Ok )
        returnValue = msgBox.exec()
        matA = ["ERROR"]
        return matA

def val_numIn(ui,val,pos):
    try:
        num =int(val)
        return num
    except(ValueError):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        if(pos==0):
            msgBox.setText("El Valor del Nodo Inicial es Invalido")
        elif(pos==1):
            msgBox.setText("El Valor del Nodo Final es Invalido")
        elif(pos==2):
            msgBox.setText("El Valor de No. de Pasos es Invalido")
        else:
            msgBox.setText("Ocurrio Algo Inesperado")
        msgBox.setWindowTitle("ERROR")
        msgBox.setStandardButtons(QMessageBox.Ok )
        returnValue = msgBox.exec()
        num="ERROR"
        return num

def error(ui,pos):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    if(pos==0):
        msgBox.setText("El Valor del Nodo Inicial está Fuera del Rango")
    elif(pos==1):
        msgBox.setText("El Valor del Nodo Final está Fuera del Rango")
    elif(pos==2):
        msgBox.setText("El Valor de No. de Pasos no Puede ser Negativo")
    else:
        msgBox.setText("Ocurrio Algo Inesperado")
    msgBox.setWindowTitle("ERROR")
    msgBox.setStandardButtons(QMessageBox.Ok )
    returnValue = msgBox.exec()

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

