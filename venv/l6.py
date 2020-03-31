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
import struct as st
##

def punto1(default=True,A=[],b=[],n=0):
    if default:
        A = np.random.rand(3,3)#matriz aleatoria de 3x3
        n= 3
        b = np.random.rand(3,1)#matriz de contantes
    m = np.concatenate((A,b),axis=1)#se crea la matriz agregada

    At = np.transpose(A)#solo se tiene en cuenta la matriz A
    max_indices = np.argmax(At,axis=1)#encuentra el indice del pivote

    #poner pivotes
    for i in range(n):
        if i <= max_indices[i]:#si ya se cambió, entonces no la tenga en cuenta
            m[[i,max_indices[i]]] = m[[max_indices[i],i]]#se intercambian las filas de acuerdo a la que sea mayor


    #gauss con unos en la diagonal
    for i in range(n):
        for j in range(n):
            if j == i:#para dejar la matriz como triangular superior
                m[i] /= m[i][j]#poner unos en la diagonal
                break
            m[i] -= m[j]*(m[j][j]*m[i][j])
            #m[j]*(m[i][j]/m[j][j])

    #gauss jordan
    for i in range(n):
        for j in range(n):
            if j <= i:#ahora toca recorrer la matriz superior
                continue
            m[i] -= m[j]*(m[j][j]*m[i][j])
    coeficientes = m[:,-1]#coeficientes que se están poniendo en donde entra el vector b
    if default:
        print(coeficientes)
        print(np.linalg.solve(A,b))
    else:
        return coeficientes

## no sé por qué no sirve con el cell block plugin. No encuentra el archivo pero corriendo todo el script sí funciona
def punto3(default=True,x=[],y=[]):
    if default:
        f = open('Lab-Reg-X.bin',"rb")
        file = f.read()
        paqueteX = st.unpack("d"*int(len(file)/8),file)
        f = open('Lab-Reg-Y.bin', "rb")
        file = f.read()
        paqueteY = st.unpack("d" * int(len(file) / 8), file)

        #como son tuplas, toca pasarla a listas y luego a arreglos de numpy
        x = np.array(list(paqueteX))
        y = np.array(list(paqueteY))
    meanX = np.mean(x)
    meanY = np.mean(y)
    N = np.size(x)

    #los valores que van en la matriz
    a2 = np.sum(x**2)/N
    b2 = np.sum(x*y)/N

    A = np.array([[1,meanX],[meanX,a2]])
    b = np.array([[meanY],[b2]])
    solucion = punto1(False,A=A,b=b,n=len(A[0]))

    p = np.polyfit(x, y, 1)
    yr = np.polyval(p,x)

    plt.figure()
    plt.plot(x,y,'.')
    plt.plot(x,yr,'g')
    plt.plot(x,solucion[1]*x+solucion[0],'r')#como es la misma linea, queda la roja superpuesta
    plt.show()

    return solucion

punto3()