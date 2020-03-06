import numpy as np
print()
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
