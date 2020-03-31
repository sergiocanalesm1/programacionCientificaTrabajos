'''
    Programación Científica
    Laboratorio 6
    Sergio Canales
    201729241
    Ingeniería de sistemas y computación
'''
##
import numpy as np
import matplotlib.pyplot as plt
##

def punto1():
    A = np.random.rand(3,3)#matriz aleatoria de 3x3
    n= 3
    b = np.random.rand(3,1)#matriz de contantes
    m = np.concatenate((A,b),axis=1)#se crea la matriz agregada

    At = np.transpose(A)#solo se tiene en cuenta la matriz A
    max_indices = np.argmax(At,axis=1)#encuentra el indice del pivote

    #poner pivotes
    for i in range(n):
        if i <= max_indices[i]:
            m[[i,max_indices[i]]] = m[[max_indices[i],i]]#se intercambian las filas de acuerdo a la que sea mayor


    #gauss con unos en la diagonal
    for i in range(n):
        for j in range(n):
            if j == i:#para dejar la matriz como triangular superior
                m[i] /= m[i][j]#poner unos en la diagonal
                break
            m[i] -= m[j]*(m[i][j]/m[j][j])

    #gauss jordan
    for i in range(n):
        for j in range(n):
            if j <= i:#ahora toca recorrer la matriz superior
                continue
            m[i] -= m[j]*(m[j][j]*m[i][j])

    print(m[:,-1])#coeficientes

def punto3():
    



punto1()