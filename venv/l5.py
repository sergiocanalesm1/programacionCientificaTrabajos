'''
    Programación Científica
    Laboratorio 5
    Sergio Canales
    Ingeniería de sistemas y computación
'''

'''
ejemplo de entrada para punto 1:

3
1 2 3 3
2 6 9 2
14 9 5 3
'''
def punto1():
    print("ingrese en la primera línea el tamaño de la matriz A y en las siguientes las filas de la matriz con columnas separadas por espacios (referir a las ejemplols)")

    n=int(input())
    mat=[]
    gauss=[]
    for _ in range(n):
        mat.append(list(map(int, input().split())))#coge cada linea y la convierte a un arreglo de enteros, luego las agrega a la matriz mat
    #gauss.append(mat[0])#toca insertar la primera fila asi para que funcione mi algoritmo
    for fIndex in range(n):
        for cIndex in range(len(mat[0])):
            if cIndex ==fIndex:
                break
            coefficient = (mat[fIndex][cIndex]/mat[cIndex][cIndex])
            print(coefficient)

            lista=[]
            for col in range(len(mat[fIndex])):
                current = mat[fIndex][col]
                restar = coefficient*mat[cIndex][col]
                lista.append(current-restar)
            mat[fIndex] = lista.copy()
            lista.clear()
            #gauss[fIndex]=[mat[fIndex][col]-coefficient*gauss[cIndex][col] for col in range(len(mat[fIndex]))]

    print(mat)
punto1()