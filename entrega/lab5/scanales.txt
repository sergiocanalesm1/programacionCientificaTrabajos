'''
    Programación Científica
    Laboratorio 5
    Sergio Canales
    201729241
    Ingeniería de sistemas y computación
'''

##
import matplotlib.pyplot as plt
import numpy as np
def punto1(default=True,A=[],b=[]):
    if default:
        A = np.random.rand(3,3)
        b = np.random.rand(3,1)
    mat = np.column_stack((A,b))
    #algoritmo
    for fIndex in range(len(mat)):
        for cIndex in range(len(mat[0])):
            if cIndex ==fIndex:
                break
            coefficient = (mat[fIndex][cIndex]/mat[cIndex][cIndex])#coeficiente para que se ponga cero en el CIndex y convierta el resto de la fila
            mat[fIndex] = [mat[fIndex][currentC]-coefficient*mat[cIndex][currentC] for currentC in range(len(mat[fIndex]))]#crea una nueva lista(fila) restando cada data (pareja fila-columna) por el coeficiente multiplicado con la fila y columna requerida

    #encontrar coeficientes
    coefficient = []
    for fIndex in range(len(mat)-1,-1,-1):
        cIndex = 2#para no contar el del vector b
        sumaLocal = 0 # aquí se guarda el valor que se va calculado de cada fila para poder calcular el coeficiente correspondiente
        #el algoritmo recorre el triangulo superior, desde la esquina de abajo, hasta la esquina de arriba a la izquierda. se calcula el de más abajo, luego ese se usa para calcular de de arriba, luego esos dos para calcular el de más arriba y así sucesivamente
        while cIndex > fIndex:
            sumaLocal += coefficient[2-cIndex]*mat[fIndex][cIndex]#usa los coeficientes ya encontrados para sumar todos los escalares hasta el "pivote"
            cIndex -= 1
        coefficient.append((mat[fIndex][-1]-sumaLocal)/mat[fIndex][cIndex])#hace la siguiente operación ax + suma(b,c,d...) = e -> x = e-suma(b,c,d...)/a
    coefficient.reverse()#como los encontró de abajo para arrba, toca voltearlo
    if default:
        print("los valores que yo calculé son:\n {} \nlos de numpy son: \n {}".format(coefficient,np.linalg.solve(A,b)))
    return coefficient
punto1()
##
import matplotlib.pyplot as plt
import numpy as np
def punto2(mostrar=True):
    '''
    print("ingrese en la primera línea el tamaño de la matriz A y en las siguientes las filas de la matriz con columnas separadas por espacios (referir a las ejemplos)")
    n=int(input())#numero de filas
    mat=[]
    A = []
    b = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))#coge cada linea y la convierte a un arreglo de enteros, luego las agrega a la matriz mat
        A.append(mat[_][:-1])#meterle todos los datos menos el último
        b.append([mat[_][-1]])#meterle el último dato
    '''
    A = np.random.rand(3, 3)
    i = np.eye(3,dtype=int)
    b = np.random.rand(3, 1)
    mat = np.column_stack((A,i,b))
    #algoritmo

    for fIndex in range(len(mat)):
        for cIndex in range(3):
            if cIndex ==fIndex:
                break
            coefficient = (mat[fIndex][cIndex]/mat[cIndex][cIndex])#coeficiente para que se ponga cero en el CIndex y convierta el resto de la fila
            mat[fIndex] = [mat[fIndex][currentC]-coefficient*mat[cIndex][currentC] for currentC in range(len(mat[fIndex]))]#crea una nueva lista(fila) restando cada data (pareja fila-columna) por el coeficiente multiplicado con la fila y columna requerida
    #hasta acá es igual al punto 1


    for fIndex in range(len(mat)-1,-1,-1):
        cIndex = 2#para no contar el del vector b
        while cIndex > fIndex:
            constante = (mat[fIndex][cIndex] / mat[cIndex][cIndex])
            mat[fIndex] = [mat[fIndex][currentC] - constante*mat[cIndex][currentC] for currentC in range(len(mat[0]))]
            cIndex -= 1

    for f in range(len(mat)):
        mat[f] = [mat[f][i]/mat[f][f] for i in range(len(mat[0]))]#poner la identidad
    #coefficients = [mat[i][-1]/mat[i][i] for i in range(len(mat))]#recorre la diagonal principal y calcula el valor del vector b tal que la identidad de A sea 1

    if mostrar:
        print("los valores que yo calculé son:\n {} \nlos de numpy son: \n {}".format(mat[:,6],np.linalg.solve(A,b)))#en la columna 6 está el vector b

    return mat[:,3:6]#de la columna 3 a la 6 está la inversa
punto2()

def punto3():
    '''
    Para el sistema matricial de la forma Ax=b:
     hay una única solución cuando A es una matriz cuadrada n*n y el vector b tiene n filas. Gráficamente (en 2-d), sucede cuando mi solución al sistema intersecta exactamente en un punto sobre mi sistema lineal
     hay infinitas soluciones cuando A es una matriz m*n y n > m, pues hay más variables que ecuaciones. Gráficamente (en 2-d), sucede cuando mi solución es paralela sobre mi sistema y está exactamente encima de él
     no hay soluciones cuando A es una matriz m*n y m > n, pues hay más ecuaciones que variables. Gráficamente (en 2-d) sucede cuando mi solución es parelela a mi sistema, con una distance de separación mayor a 0
    '''

    pass
##
import matplotlib.pyplot as plt
import numpy as np
def punto4(): #(-2, 0), (-7, 1) y (5, -1)
    A = np.array([[-2,0,1],[-7,1,1],[5,-1,1]])
    b = np.array([[-4],[-50],[-26]])
    sol = punto1(default=False,A=A,b=b)
    print(sol)
    print(np.linalg.solve(A,b))
    '''
    https://www.mathsisfun.com/algebra/circle-equations.html
    
    x^2 + y^2 + Ax + By + C = 0
        <para completar el cuadrado>
    x^2 + Ax + y^2 + By + C = 0
        <aritmética: sumar (A/2)^2 a los dos lados para completar el cuadrado de (x+A/2)^2>
    x^2 + Ax + (A/2)^2 + y^2 + By + C = (A/2)^2 
        <aritmética: sumar (B/2)^2 a los dos lados para completar el cuadrado de (y+B/2)^2>
    x^2 + Ax + (A/2)^2 + y^2 + By + (B/2)^2 + C = (A/2)^2+ (B/2)^2 
        <factorizar>
    (x+A/2)^2 + (y+B/2)^2 + C = (A/2)^2+ (B/2)^2
        <reemplazando los valores de la solución obtenida en este punto [-34.0, -216.0, -72.0]>
    (x-34/2)^2 + (y-216/2)^2 -72 = (-34/2)^2 + (-216/2)^2
        <aritmética>
    (x-17)^2 + (y-108)^2 -72 = 17^2 + 108^2
        <aritmética>
    x^2-289 + y^2-11664 -72 = 289 + 11664
        <aritmética>
    x^2 + y^2 = 289 + 11664 + 72 + 11664 + 289
        <aritmética>
    x^2 + y^2 = 23978
    
    r^2 = 23978
    '''
    r = (23978)**(1/2)
    plt.figure()
    x = np.linspace(0, 2*np.pi,50)
    plt.plot(r*np.cos(x),r*np.sin(x),".g")#polares
    plt.show()
punto4()

##
import matplotlib.pyplot as plt
import numpy as np
def punto5():
    #se evalua cada punto para construir la matriz
    a = np.array([(-2.68)**4,(-2.68)**3,(-2.68)**2,(-2.68),1])
    e = np.array([(-3.25)**4,(-3.25)**3,(-3.25)**2,(-3.25),1])
    i = np.array([(-4.45) ** 4, (-4.45) ** 3, (-4.45) ** 2, (-4.45), 1])
    o = np.array([(-6.25) ** 4, (-6.25) ** 3, (-6.25) ** 2, (-6.25), 1])
    u = np.array([(-8.15) ** 4, (-8.15) ** 3, (-8.15) ** 2, (-8.15), 1])
    A = np.array([a,e,i,o,u])
    b=np.array([[0],[1.25],[-1.56],[-2.84],[0.23]])
    #sol=punto1(False,A,b)
    sol=np.linalg.solve(A,b)
    x = np.arange(-8.15 ,-2.68,0.1)
    plt.figure()
    plt.plot(x,x**4*sol[0]+x**3*sol[1]+x**2*sol[2]+x*sol[3]+sol[4])
    plt.show()
punto5()
