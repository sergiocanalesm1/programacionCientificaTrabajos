'''
Sergio Canales
Universidad de los Andes
Programación Científica
'''

import numpy as np
import matplotlib.pyplot as plt

#1. escriba una funcion que sume todos los datos de un arreglo
def uno():
    print('ingrese numeros separados por un espacio para calcular su suma')
    entra = input().split()
    list = list(map(float,entra))#se convierten todos los valores a float y se pasan a una lista
    print(sum(list))
#2. escriba una funcion que calcule el factorial de un numero
def dos():
    print('ingrese un numero para calcular su factorial')
    n = int(input())
    print(factorial(n))
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
#3. escriba una funcion que diga si un numero es primo
def tres():
    print('ingrese un numero para verificar si es primo')
    n = int(input())
    print(primo(n,2))
def primo(n,x):
    if x > n**(1/2):#mira hasta la raiz cuadrada del numero a verificar
        return True
    elif not n % x:#si es divisible por x, no es primo
        return False
    else:
        return primo(n,x+1)#sigue verificando

#4. escriba una funcion que diga si una cadena de caracteres es polindroma
def cuatro():
    print('ingrese una cadena de caracteres para verificar si es polindroma')
    entra = input().split()
    cadena = "".join(entra).casefold() #para quitar los espacios y casefold para poner todo en minusculas y no tener problemas comparando
    print(polindroma(cadena,cadena[0],cadena[-1],0))
def polindroma(cadena,recorridoNormal,recorridoInverso,contador):
    if recorridoNormal != recorridoInverso:#si los caracteres a comparar son diferentes, no es palidroma
        return False
    elif contador == len(cadena) -1:#para ver si ya termino de comparar
        return True
    else:
        contador += 1
        return polindroma(cadena,cadena[contador],cadena[-contador-1],contador)#comparar los siguientes caracteres

#5. escriba una funcion que determine si un entero positivo pertence a la serie de fibonaci
def cinco():
    print('ingrese un numero entero positivo para determinar si pertenece a la serie de fibonacci')
    n = int(input())
    if n == 1:
        print(True)
    elif n == 0:
        print(False)
    else:
        print(fibonacci(1,1,n))
def fibonacci(f_x1,f_x2,numero_usuario):
    if f_x1 >= numero_usuario or f_x2 >= numero_usuario:#si la suma ya se pasa, no pertenece a fibonacci
        return False
    elif f_x1 + f_x2 == numero_usuario:
        return True
    else:
        return fibonacci(f_x2,f_x1 + f_x2,numero_usuario) #el primer valor se convierte en el que estaba de segundo y el segundo se convierte en la suma de los primeros dos

#6. escriba una función que calcule la media de las filas o columnas de una matriz
def seis():
    print("escriba un n para ingresar n número de listas")
    n = int(input())
    matriz = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números".format(x+1,n,n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        lista = list(map(int,ingreso))
        matriz.append(lista.copy())#para agregar lo que ingresa el usuario a la matriz
        lista.clear()#para usar la misma lista (gracias al .copy())
    print("desea calcular la media según filas o columnas? ingrese F o C")
    criterio = input()
    if "F" != criterio and "C" != criterio:
        print("ingrese F o C, nada más")
        return None
    if criterio == "F":
        for fila in matriz:
            print("el promedio de la fila {} es : {}".format(fila,sum(fila)/n))
    else:
        for cIndex in range(n):
            columna = []
            for fIndex in range(n):
                columna.append(matriz[fIndex][cIndex])#el cIndex se queda fijo por cada lista, esto nos da la columna al final de la iteración
            print(" el promedio de la columna {} es {}".format(columna, sum(columna)/n))
            columna.clear()  # se crea una lista con la columna de la matriz, se encuentra el promedio y se borra

#7. ingrese una función que de el máximo de cada fila o columna en una matriz
def siete():
    print("escriba un n para ingresar n número de listas")
    n = int(input())
    matriz = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números".format(x+1,n,n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        lista = list(map(int,ingreso))
        matriz.append(lista.copy())#para agregar lo que ingresa el usuario a la matriz
        lista.clear()#para usar la misma lista (gracias al .copy())
    print("desea calcular el máximo según filas o columnas? ingrese F o C")
    criterio = input()
    if "F" != criterio and "C" != criterio:
        print("ingrese F o C, nada más")
        return None
    if criterio == "F":
        for fila in matriz:
            print("el máximo de la fila {} es : {}".format(fila, max(fila)))
    else:
        for cIndex in range(n):
            columna = []
            for fIndex in range(n):
                columna.append(matriz[fIndex][cIndex])#el cIndex se queda fijo por cada lista, esto nos da la columna al final de la iteración
            print(" el máximo de la columna {} es {}".format(columna, max(columna)))
            columna.clear()#se crea una lista con la columna de la matriz, se encuentra el máximo y se borra

#8. cree una función que calcule el minimo de una matriz por filas o columnas
def ocho():
    print("escriba un n para ingresar n número de listas")
    n = int(input())
    matriz = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números".format(x + 1, n, n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        lista = list(map(int, ingreso))
        matriz.append(lista.copy())  # para agregar lo que ingresa el usuario a la matriz
        lista.clear()  # para usar la misma lista (gracias al .copy())
    print("desea calcular el máximo según filas o columnas? ingrese F o C")
    criterio = input()
    if "F" != criterio and "C" != criterio:
        print("ingrese F o C, nada más")
        return None
    if criterio == "F":
        for fila in matriz:
            print("el mínimo de la fila {} es : {}".format(fila, min(fila)))
    else:
        for cIndex in range(n):
            columna = []
            for fIndex in range(n):
                columna.append(matriz[fIndex][cIndex])#el cIndex se queda fijo por cada lista, esto nos da la columna al final de la iteración
            print(" el mínimo de la columna {} es {}".format(columna, min(columna)))
            columna.clear()  # se crea una lista con la columna de la matriz, se encuentra el mínimo y se borra

#9. cree una función que sume elemento por elemento dos matrices
def nueve():
    print("escriba un n para ingresar n número de listas para la matriz 1")
    n = int(input())
    matriz = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números para la matriz 1".format(x + 1, n, n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        lista = list(map(int, ingreso))
        matriz.append(lista.copy())  # para agregar lo que ingresa el usuario a la matriz
        lista.clear()  # para usar la misma lista (gracias al .copy())
    print("escriba un n para ingresar n número de listas para la matriz 2")
    n = int(input())
    matriz2 = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números para la matriz 2".format(x + 1, n, n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        lista = list(map(int, ingreso))
        matriz2.append(lista.copy())  # para agregar lo que ingresa el usuario a la matriz
        lista.clear()  # para usar la misma lista (gracias al .copy())

    sumMatriz = []
    for fIndex in range(n):
        fila = []
        for cIndex in range(n):
            suma = matriz[fIndex][cIndex] + matriz2[fIndex][cIndex]
            fila.append(suma)
        sumMatriz.append(fila.copy())
        fila.clear()
    print(sumMatriz)

#10. escriba una función que calcule una multiplicación de matrices
def diez():
    print("escriba un n para ingresar n número de listas para la matriz 1")
    n = int(input())
    matriz = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números para la matriz 1".format(x + 1, n,
                                                                                                               n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        matriz.append(list(map(int, ingreso)))
    print("escriba un n para ingresar n número de listas para la matriz 2")
    n = int(input())
    matriz2 = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números para la matriz 2".format(x + 1, n,
                                                                                                               n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        matriz2.append(list(map(int, ingreso)))
    newMatrix = []
    for fIndex in range(n):
        lista = []
        for cIndex in range(n):
            sum_product = 0
            for iterable in range(n):
                    sum_product += matriz[fIndex][iterable] * matriz2[iterable][cIndex] #solo se necesita un for que en la matriz uno recorra la fila general (moviendose por todas las columnas) y en la matriz 2 la columna general (moviendose por todas las filas)
            lista.append(sum_product)
        newMatrix.append(lista.copy())
        lista.clear()
    print(newMatrix)





#11. del 6-10 con numpy
#escriba una función que calcule la media de las filas o columnas de una matriz
def once6():
    print("escriba un n para ingresar n número de listas")
    n = int(input())
    matriz = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números".format(x + 1, n, n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        matriz.append(list(map(int, ingreso)))
    arr = np.array(matriz)
    print("desea calcular la media según filas o columnas? ingrese F o C")
    criterio = input()
    if "F" != criterio and "C" != criterio:
        print("ingrese F o C, nada más")
        return None
    if criterio == "F":
        for fila in arr:
            print("el promedio de la fila {} es : {}".format(fila, np.mean(fila)))
    else:
        t = arr.transpose()#para poder iterar las columnas
        for columna in t:
            print(" el promedio de la columna {} es {}".format(columna, np.mean(columna)))




#ingrese una función que de el máximo de cada fila o columna en una matriz
def once7():
    print("escriba un n para ingresar n número de listas")
    n = int(input())
    matriz = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números".format(x + 1, n, n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        matriz.append(list(map(int, ingreso)))
    arr = np.array(matriz)
    print("desea calcular el máximo según filas o columnas? ingrese F o C")
    criterio = input()
    if "F" != criterio and "C" != criterio:
        print("ingrese F o C, nada más")
        return None
    if criterio == "F":
        for fila in arr:
            print("el máximo de la fila {} es : {}".format(fila, fila.max())) #da el máximo del arreglo
    else:
        t = arr.transpose()#para poder iterar las columnas
        for columna in t:
            print(" el máximo de la columna {} es {}".format(columna, columna.max())) #da el máximo del arreglo

#el mínimo
def once8():
    print("escriba un n para ingresar n número de listas")
    n = int(input())
    matriz = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números".format(x + 1, n, n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        matriz.append(list(map(int, ingreso)))
    arr = np.array(matriz)
    print("desea calcular el mínimo según filas o columnas? ingrese F o C")
    criterio = input()
    if "F" != criterio and "C" != criterio:
        print("ingrese F o C, nada más")
        return None
    if criterio == "F":
        for fila in arr:
            print("el mínimo de la fila {} es : {}".format(fila, fila.min()))
    else:
        t = arr.transpose()#para poder iterar las columnas
        for columna in t:
            print(" el promedio de la columna {} es {}".format(columna, columna.min()))
#sumar elemento por elemento
#arr = np.array(matriz) #para convertirlo en un ndarray
def once9():
    print("escriba un n para ingresar n número de listas para la matriz 1")
    n = int(input())
    matriz = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números para la matriz 1".format(x + 1, n, n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        matriz.append(list(map(int, ingreso)))
    print("escriba un n para ingresar n número de listas para la matriz 2")
    n = int(input())
    matriz2 = []
    for x in range(n):
        print("ingrese la lista {} (separada por espacios) de {} listas con n números para la matriz 2".format(x + 1, n, n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        matriz2.append(list(map(int, ingreso)))
    arr1 = np.array(matriz)
    arr2 = np.array(matriz2)
    print("\n la suma de las matrices es: {}".format(np.add(arr1,arr2)))

#producto matricial
def once10():
    print("escriba un n para ingresar n número de listas para la matriz 1")
    n = int(input())
    matriz = []
    for x in range(n):
        print(
            "ingrese la lista {} (separada por espacios) de {} listas con n números para la matriz 1".format(x + 1,
                                                                                                             n, n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        matriz.append(list(map(int, ingreso)))
    print("escriba un n para ingresar n número de listas para la matriz 2")
    n = int(input())
    matriz2 = []
    for x in range(n):
        print(
            "ingrese la lista {} (separada por espacios) de {} listas con n números para la matriz 2".format(x + 1,
                                                                                                             n, n))
        ingreso = input().split()
        if len(ingreso) != n:
            print("por favor, ingrese lo especificado")
            return None
        matriz2.append(list(map(int, ingreso)))
    arr1 = np.array(matriz)
    arr2 = np.array(matriz2)
    print("\n la suma de las matrices es: {}".format(arr1 @ arr2))

def doce():
    #for x in range(1,11):
    a =  np.linspace(0,10,100)
    ran = np.sin(a*10/(2*np.pi)    )
    plt.figure()
    plt.plot(a,ran)
    plt.title("sine")
    plt.show()
doce()


