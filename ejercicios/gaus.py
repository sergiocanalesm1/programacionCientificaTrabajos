import numpy as np
import matplotlib.pyplot as plt
def gauss(matriz):

    pass
'''
1) poner 0 en la primera posición de la segunda fila
    a) restarle una combinación lineal de la primera fila a las segunda tal que me ponga 0 en la primera posición
        i) fil2Col1 -= fil1Col1*(fil2Col1/fil1Col1) y hacer eso para todas las columnas de la fila 2 
2) poner 0 en la primera posición de la tercera fila
    a) restarle una combinación lineal de la primera fila a las tercer tal que me ponga 0 en la primera posición
        i) fil3Col1 -= fil1Col1*(fil3Col1/fil1Col1) y hacer eso para todas las columnas de la fila 2
    b)  restarle una combinación lineal de la segunda fila a las tercera tal que me ponga 0 en la segunda posición
        i)fil3Col2 -= fil2Col2*(fil3Col2/fil2Col2) y hacer esto para el resto de las columnas en la fila 3
...
n) filaN: poner 0 en todas las posiciones a la izquierda de la columna N
    a) restar una combinación lineal de la filaX a la filaN tal que la columnaX de mi filaN quede en 0
        c)  filNColX -= filXColX*(filNColX/filXColX) y hacer eso para el resto de columnas de la fila N

'''
def sistema_lineal():
    N = 100
    x = np.sort(np.random.rand(N)*100)
    y = np.sort(np.random.rand(N)*100)
    A = [[1,np.mean(x)],[np.mean(x), (1/N)*np.sum(x**2)]]
    b = [[np.mean(y)],[(1/N)*np.sum(x*y)]]
    c= np.linalg.solve(A,b)#resolver un sistema lineal

    numpySol = np.polyfit(x,y,1)
    print("mio: {} \n numpy: {}".format(c, numpySol))

    recta = np.polyval(x,numpySol)
    print(recta)
    plt.figure()
    plt.plot(x,y,".r")
    toplot=  recta[0]*x+recta[1]
    #print(toplot)
    plt.plot(x,toplot,"b")
    plt.show()

sistema_lineal()
