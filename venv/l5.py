'''
    Programación Científica
    Laboratorio 5
    Sergio Canales
    Ingeniería de sistemas y computación
'''

'''
ejemplos de entrada para punto 1:

3
1 2 3 3
2 6 9 2
14 9 5 3


3
3 2 1 1
2 6 9 1
1 9 5 1

'''
#es necesario correr esta función sin cellblock, para que ingresar la matriz sea más fácil
import numpy as np
def punto1():
    print("ingrese en la primera línea el tamaño de la matriz A y en las siguientes las filas de la matriz con columnas separadas por espacios (referir a las ejemplos)")
    n=int(input())#numero de filas
    mat=[]
    A = []
    b = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))#coge cada linea y la convierte a un arreglo de enteros, luego las agrega a la matriz mat
        A.append(mat[_][:-1])#meterle todos los datos menos el último
        b.append([mat[_][-1]])#meterle el último dato
    #algoritmo
    for fIndex in range(n):
        for cIndex in range(len(mat[0])):
            if cIndex ==fIndex:
                break
            coefficient = (mat[fIndex][cIndex]/mat[cIndex][cIndex])#coeficiente para que se ponga cero en el CIndex y convierta el resto de la fila
            mat[fIndex] = [mat[fIndex][currentC]-coefficient*mat[cIndex][currentC] for currentC in range(len(mat[fIndex]))]#crea una nueva lista(fila) restando cada data (pareja fila-columna) por el coeficiente multiplicado con la fila y columna requerida

    #encontrar coeficientes
    coefficient = []
    for fIndex in range(len(mat)-1,-1,-1):
        cIndex = len(mat[0])-2#para no contar el del vector b
        sumaLocal = 0 # aquí se guarda el valor que se va calculado de cada fila para poder calcular el coeficiente correspondiente
        #el algoritmo recorre el triangulo superior, desde la esquina de abajo, hasta la esquina de arriba a la izquierda. se calcula el de más abajo, luego ese se usa para calcular de de arriba, luego esos dos para calcular el de más arriba y así sucesivamente
        while cIndex > fIndex:
            sumaLocal += coefficient[len(mat[0])-2-cIndex]*mat[fIndex][cIndex]#usa los coeficientes ya encontrados para sumar todos los escalares hasta el "pivote"
            cIndex -= 1
        coefficient.append((mat[fIndex][-1]-sumaLocal)/mat[fIndex][cIndex])#hace la siguiente operación ax + suma(b,c,d...) = e -> x = e-suma(b,c,d...)/a
    coefficient.reverse()#como los encontró de abajo para arrba, toca voltearlo
    print("los valores que yo calculé son:\n {} \nlos de numpy son: \n {}".format(coefficient,np.linalg.solve(A,b)))



def punto2():
    print("ingrese en la primera línea el tamaño de la matriz A y en las siguientes las filas de la matriz con columnas separadas por espacios (referir a las ejemplos)")
    n=int(input())#numero de filas
    mat=[]
    A = []
    b = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))#coge cada linea y la convierte a un arreglo de enteros, luego las agrega a la matriz mat
        A.append(mat[_][:-1])#meterle todos los datos menos el último
        b.append([mat[_][-1]])#meterle el último dato
    #algoritmo
    for fIndex in range(n):
        for cIndex in range(len(mat[0])):
            if cIndex ==fIndex:
                break
            coefficient = (mat[fIndex][cIndex]/mat[cIndex][cIndex])#coeficiente para que se ponga cero en el CIndex y convierta el resto de la fila
            mat[fIndex] = [mat[fIndex][currentC]-coefficient*mat[cIndex][currentC] for currentC in range(len(mat[fIndex]))]#crea una nueva lista(fila) restando cada data (pareja fila-columna) por el coeficiente multiplicado con la fila y columna requerida
    #hasta acá es igual al punto 1


    for fIndex in range(len(mat)-1,-1,-1):
        cIndex = len(mat[0])-2#para no contar el del vector b
        while cIndex > fIndex:
           # mat[fIndex][cIndex] = mat[fIndex][cIndex] - (mat[cIndex][cIndex]/mat[fIndex][cIndex])*mat[currentC][cIndex]
            cIndex -= 1
    print(mat)
    coefficients = [mat[i][-1]/mat[i][i] for i in range(len(mat))]#recorre la diagonal principal y calcula el valor del vector b tal que la identidad de A sea 1

    print("los valores que yo calculé son:\n {} \nlos de numpy son: \n {}".format(coefficients,np.linalg.solve(A,b)))

punto2()
#para el punto 4 y 5 toca usar polares. rcos y rsen