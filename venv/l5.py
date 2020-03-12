'''
    Programación Científica
    Laboratorio 5
    Sergio Canales
    Ingeniería de sistemas y computación
'''

'''
ejemplos de entrada para punto 1:

4
1 2 3 3
2 6 9 2
14 9 5 3
1 2 3 4

3
3 2 1 
2 6 9 
14 9 5 

'''
def punto1():
    print("ingrese en la primera línea el tamaño de la matriz A y en las siguientes las filas de la matriz con columnas separadas por espacios (referir a las ejemplols)")
    n=int(input())#numero de filas
    mat=[]
    for _ in range(n):
        mat.append(list(map(int, input().split())))#coge cada linea y la convierte a un arreglo de enteros, luego las agrega a la matriz mat
    #algoritmo
    for fIndex in range(n):
        for cIndex in range(len(mat[0])):
            if cIndex ==fIndex:
                break
            coefficient = (mat[fIndex][cIndex]/mat[cIndex][cIndex])#coeficiente para que se ponga cero en el CIndex y convierta el resto de la fila
            mat[fIndex] = [mat[fIndex][currentC]-coefficient*mat[cIndex][currentC] for currentC in range(len(mat[fIndex]))]#crea una nueva lista(fila) restando cada data (pareja fila-columna) por el coeficiente multiplicado con la fila y columna requerida
    print(mat)


punto1()
#para el punto 4 y 5 toca usar polares. rcos y rsen