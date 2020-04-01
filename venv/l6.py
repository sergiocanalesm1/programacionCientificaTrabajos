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


def punto1(default=True,A=[],b=[],n=0):
    if default:
        A = np.random.rand(3,3)#matriz aleatoria de 3x3
        n= 3
        b = np.random.rand(3,1)#matriz de contantes
    m = np.concatenate((A,b),axis=1)#se crea la matriz agregada

    At = np.transpose(A)#solo se tiene en cuenta la matriz A
    max_indices = np.argmax(np.abs(At),axis=1)#encuentra el indice del pivote

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
        print("mis coeficientes son:\n",coeficientes,"\n")
        print("los coeficientes de numpy son:\n",np.linalg.solve(A,b))
    else:
        return coeficientes

# no sé por qué no sirve con el cell block plugin. No encuentra el archivo pero corriendo todo el script sí funciona
def punto3():

    f = open('Lab-Reg-X.bin',"rb")
    file = f.read()
    paqueteX = st.unpack("d"*int(len(file)/8),file)
    f.close()
    f = open('Lab-Reg-Y.bin', "rb")
    file = f.read()
    paqueteY = st.unpack("d" * int(len(file) / 8), file)
    f.close()

    #como son tuplas, toca pasarla a listas y luego a arreglos de numpy
    x = np.array(list(paqueteX))
    y = np.array(list(paqueteY))

    solucion = regresion(x,y)

    p = np.polyfit(x, y, 1)
    print("mis coeficientes son: m = {} y b = {} \n".format(solucion[1],solucion[0]) )
    print("los coeficientes de numpy son: m = {} y b = {} \n".format(p[0],p[1]) )
    yr = np.polyval(p,x)

    plt.figure()
    plt.plot(x,y,'.')
    plt.plot(x,yr,'g')
    plt.plot(x,solucion[1]*x+solucion[0],'r')#como es la misma linea, queda la roja superpuesta
    plt.show()

    return solucion

def regresion(x,y):
    meanX = np.mean(x)
    meanY = np.mean(y)
    N = np.size(x)

    # matriz para coeficientes de regresion lineal
    A = np.array([[1, meanX], [meanX, np.sum(x ** 2) / N]])
    b = np.array([[meanY], [np.sum(x * y) / N]])

    return punto1(False, A=A, b=b, n=len(A[0]))

def punto4():
    women = np.array([12.20,11.90,11.50,11.90,11.50,11.50,11.00,11.40,11.08,11.07,11.08,11.06,10.97,10.54,10.82,10.94,10.75,10.93])
    men = np.array([10.80,10.30,10.30,10.30,10.40,10.50,10.20,10.00,9.95,10.14,10.06,10.25,9.99,9.92,9.96,9.84,9.87,9.85])
    years = np.array([1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004])
    solMen = regresion(years,men)
    solWomen = regresion(years,women)
    m1 = solMen[1]
    b1 = solMen[0]
    m2 = solWomen[1]
    b2 = solWomen[0]

    pM = np.polyfit(years,men,1)
    pW = np.polyfit(years,women,1)
    print("Hombres: mis coeficientes son: m = {} y b = {} y los de numpy son m = {} y b = {}\n".format(m1, b1,pM[0], pM[1]))
    print("Mujeres: mis coeficientes son: m = {} y b = {} y los de numpy son m = {} y b = {}".format(m2, b2,pW[0], pW[1]))

    intersectionX = (b2-b1)/(m1-m2)
    intersectionY = m1*intersectionX+b1

    domain = np.arange(1928,2200,4)
    plt.figure()
    plt.axis([1928, 2200, 0, 15])
    plt.plot(years,women,".g",label="women data")
    plt.plot(years,men,".b",label="men data")
    plt.plot(domain, m1*domain+b1,"b",label="men regression")
    plt.plot(domain, m2*domain + b2,"g",label="women regression")
    plt.plot(intersectionX,intersectionY,"ro",label="intersection")
    plt.text(intersectionX-20,intersectionY+1,"({} , {})".format(round(intersectionX,2),round(intersectionY,2)))
    plt.legend(loc='lower left')
    plt.show()
punto4()