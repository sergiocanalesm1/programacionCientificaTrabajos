# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import math


# 1 Escriba un programa que pregunte el radio de un círculo y calcule el área

def uno():
    print("Escriba el radio para calcular el área de un círulo")
    radio = float(input())
    #se usa la librería math para acceder a la constate pi
    area = math.pi * (radio ** 2)
    print("el area del círculo con radio {} es: ".format(radio, area))


# 2 Escriba un programa que pregunte el nombre y apellido y los imprima en orden contrario

def dos():
    print("escriba su nombre y su apellido separados por un espacio para cambiarles el orden")
    nombreYapellido = input()
    #se separa el string que entra y se invierte
    nombre = nombreYapellido.split(" ")[0]
    apellido = nombreYapellido.split(" ")[1]
    print("{} {}".format(apellido, nombre))


# Escriba un programa que pregunte un número n y calcule el valor de n+n*n+n*n*n.

def tres():
    print("escriba un número n para calcular n+n*n+n*n*n")
    n = float(input())
    print(n ** 3 + n ** 2 + n)


# Escriba un programa que calcule el número de días entre dos fechas en formato AAAA-MM-DD.
def cuatro():
    print("escriba dos fechas en formato AAAA-MM-DD separadas por un espacio para calcular la diferencia de días")
    fechas = input()
    # se separa el string inicial para obtener las dos fechas
    primera = fechas.split()[0]
    segunda = fechas.split()[1]
    #se saca la diferencia entre los años, meses y días al  separar cada fecha por su año, mes y día y restar
    años = int(primera.split("-")[0]) - int(segunda.split("-")[0])
    meses = int(primera.split("-")[1]) - int(segunda.split("-")[1])
    dias = int(primera.split("-")[2]) - int(segunda.split("-")[2])
    #se multiplica la diferencia por su unidad
    diferencia = abs(años * 365 + meses * 30 + dias)

    print(
        "asumiendo que un año tiene 365 días y que un mes tiene 30 días, la diferencia absoluta entre las fechas es: {} día(s)".format(
            diferencia))


# Escriba un programa que pregunte el radio de una esfera y calcule el volumen.
def cinco():
    print("escriba el radio de una esfera para calcular su volumen")
    radio = float(input())
    #se utiliza la librería math para obtener pi
    volumen = (4 / 3) * math.pi * radio ** 3
    print("el volumen de la esfera con radio {} es: {}".format(radio, volumen))


# Escriba un programa que calcule la diferencia entre un número n y 12. Si la diferencia es mayor que
def seis():
    print("escriba un número entero para calcular su diferencia con 12")
    n = int(input())

    if abs(12-n) > 12:
        print("como la magnitud de la diferencia de {} y 12 es mayor a 12, su diferencia absoluta al cuadrado es: {}".format(n, (n - 12) ** 2))
    else:
        print("la diferencia entre 12 y {} es: {}".format(n, 12 - n))


# Escriba un programa que verifique si un número es menor que 100 o está entre 100 y 1000 o entre
# 1000 y 2000 o es mayor que 2000.
def siete():
    print("ingrese un número para verificar su rango")
    n = int(input())
    if n < 100:
        print("{} < 100".format(n))
    elif n in range(100, 1001):
        print("100 <= {} <= 1000".format(n))
    elif n in range(1001, 2001):
        print("1001 < {} <= 2000".format(n))
    else:
        print("2000 < {}".format(n))


def ocho():
    print("ingrese un número entero para ver si es impar")
    n = int(input())
    #si no hay residuo, es par
    if n % 2 == 0:
        print("par")
    else:
        print("impar")


# Escriba un programa que cuente el número de veces que se repite el número n en un arreglo
def nueve():
    print("escriba un número para saber su ocurrencia en una lista")
    n = input()
    print("ingrese la lista de números separados por comas")
    string = input()
    arreglo = string.split(",")
    #se recorre el arreglo y se verifica la ocurrencia de la variable n
    contador=0
    for i in arreglo:
        if i == n:
            contador+=1
    print("{} aparece {} veces en {}]".format(n, contador,arreglo))


def diez():
    print("ingrese una cadena de caracteres")
    cadena = input()
    print(
        "ingrese un n entero para mostrar los últimos n caracteres de la cadena. El número tiene que ser menor o igual al tamaño de la cadena")
    n = int(input())
    #el siguiente rango coge los últimos n caracteres de la cadena
    print("los últimos {} caracteres de la cadena {}, son: {}".format(n, cadena, cadena[-n:]))


def once():
    print("ingrese 3 números separados por un espacio para calcular su suma, de ser iguales, debe retornar 0")
    numerosString = input().split()
    #se convierten los caracteres a enteros usando map
    numeros = list(map(int, numerosString))
    if numeros[0] == numeros[1] == numeros[2]:
        print(0)
    else:
        print(numeros[0] + numeros[1] + numeros[2])


def doce():
    print("escriba dos números separados por un espacio para calcular su suma, si está [15,20], devuelve 20")
    numerosString = input().split()
    #se pasan los caracteres a map
    numeros = list(map(int, numerosString))
    #se suman los números de la lista numeros
    suma = 0
    for i in numeros:
        suma += i
    #valida el rango para ver si devuelve la suma o 20
    if suma in range(15, 21):
        print(20)
    else:
        print(suma)
# Escriba un programa que devuelva la siguiente operación entre dos números: (x + y) * (x + y).
def trece():
    print("ingrese dos números separados por un espacio para calcular (x + y) * (x + y)")
    inp = input().split()
    x = int(inp[0])
    y = int(inp[1])
    op = (x + y) ** 2
    print(" ({} + {}) ^ 2 es: {}".format(x,y,op))
#Escriba un programa que devuelva la distancia Euclidiana entre dos puntos x1, y1) y (x2, y2)
def catorce():
    print("ingrese dos puntos cardinales en el siguiente formato: x1 y1 x2 y2 para calcular la distancia Euclidiana")
    numerosString = input().split()
    numeros = list(map(int, numerosString))
    #se utiliza la ecuación
    distanciaEuclidiana = ((numeros[3]-numeros[1])**2+(numeros[2]-numeros[0])**2)**(1/2)
    print("la distancia euclidiana entre {} y {}, es: {}".format(numeros[0:2],numeros[2:],distanciaEuclidiana))

def quince():
    print("ingrese un número de segundos para convertirlo en días, horas, minutos y segundos")
    segundosTotales = input()
    segundos = int(segundosTotales)
    tiempo = [86400,3600,60]
    respuesta = []
    #itera sobre el dias, horas y minutos y le va quitando el valor convertido a la variable segundos
    for x in tiempo:
        aQuitar = int(segundos / x)
        respuesta.append(aQuitar)
        segundos -= aQuitar*x

    print("{} segundo(s) son: {} día(s), {} hora(s), {} minuto(s) y {} segundo(s)".format(segundosTotales,respuesta[0],respuesta[1],respuesta[2],segundos))

def dieciseis():
    print("ingrese un número hasta el cual quiera obtener todos los primos anteriores")
    n = int(input())
    primos = []
    for posiblesPrimos in range(2,n):
        esPrimo = True
        for divisor in range(2,posiblesPrimos):
            if posiblesPrimos % divisor == 0:
                esPrimo = False
                #se sale para no seguir preguntado
                break
        #si hace todo el ciclo anterior y no se modifió la variable esPrimo, entonces se agrega a la lista de primos
        if esPrimo:
            primos.append(posiblesPrimos)
    print(primos)

def diecisiete():
    print("ingrese un número para ver todos los anteriores")
    n = int(input())
    #se agregan todos a una lista para imprimirlos después
    #todosLosAnteriores = [x for x in range(n+1)]
    todosLosAnteriores = []
    for x in range(n+1):
        todosLosAnteriores.append(x)
    print(todosLosAnteriores)

def dieciocho():
    print("ingrese una lista de números separados por un espacio para encontrar el máximo")
    numerosString = input().split()
    numeros = list(map(int, numerosString))
    max = -2^64 #el minimo creo
    #itera sobre el arreglo y guarda una variable con el máximo, de encontrar uno mayor, se modifica
    for n in numeros:
        if n > max:
            max = n
    print("el número más grande es: ", max)

def diecinueve():
    print("ingrese una lista de números separados por un espacio para encontrar el mínimo")
    numerosString = input().split()
    numeros = list(map(int, numerosString))
    min = 2^64 #el maximo creo
    # itera sobre el arreglo y guarda una variable con el mínimo, de encontrar uno menor, se modifica
    for n in numeros:
        if n < min:
            min = n
    print("el número más pequeño es: ", min)

def veinte():
    print("ingrese una lista de números separados por un espacio para encontrar el promedio")
    numerosString = input().split()
    numeros = list(map(int, numerosString))
    suma = 0
    #suma todos los números de arreglo y después lo divide por el tamaño
    for n in numeros:
        suma += n
    print("el promedio es: ", suma/len(numeros))
def veintiuno():
    print("ingrese una lista de números separados por un espacio para encontrar la desviación estándar")
    numerosString = input().split()
    numeros = list(map(int, numerosString))
    suma = 0
    # suma todos los números de arreglo y después lo divide por el tamaño para optener el promedio
    for n in numeros:
        suma += n
    promedio = suma / len(numeros)
    #recorre la lista para calcular la desviación estandar
    varianza = 0
    for n in numeros:
        #se calcula qué tan alejados estan los datos del promedio al cuadrado
        varianza += (n-promedio)**2
    # se calcula qué tan alejados estan los datos del promedio, en promedio
    varianza /= len(numeros) -1
    print("la desviación estándar es: ", varianza**(1/2))
def veintidos():
    print("ingrese una lista de números separados por un espacio para encontrar la mediana")
    numerosString = input().split()
    numeros = list(map(int, numerosString))
    #algoritmo de selección sobre un mismo arreglo
    #coge un elemento y lo compara contra todos. Escoge el menor y lo pone en esa posición, ordena ascendentemente
    for iAordenar in range(len(numeros)):
        min = numeros[iAordenar]
        minIndex = 0
        for iAcomparar in range(iAordenar + 1, len(numeros)):
            if numeros[iAcomparar] < min:
                min = numeros[iAcomparar]
                minIndex = iAcomparar
        if min != numeros[iAordenar]:
            #swap, si es el menor encontrado, se intercambia
            numeros[iAordenar],numeros[minIndex] = numeros[minIndex],numeros[iAordenar]
    #si es par hace el promedio entre los dos de la mitad, si es impar coge el de la mitad
    mitad = int(len(numeros)/2)
    if len(numeros) % 2 != 0:
        mediana = numeros[mitad]
    else:
        mediana = numeros[mitad-1] + numeros[mitad]
        mediana /= 2
    print("la lista ordenada es {} y la mediana es: {}".format(numeros,mediana))

def veintitres():
    print("ingrese una lista de números separados por un espacio para encontrar la moda")
    numerosString = input().split()
    numeros = list(map(int, numerosString))
    moda = 0
    repeticionesGlobal = 0
    #recorre el arreglo n^2 veces para encontrar cuanto se repite cada posición, luego se compara contra el que más haya tenido y de ser mayor, se modifica
    for posibleModa in numeros:
        repeticionesLocal = 0
        for posibleRepeticion in numeros:
            if posibleRepeticion == posibleModa:
                repeticionesLocal+=1
        if repeticionesLocal > repeticionesGlobal:
            moda = posibleModa
            repeticionesGlobal = repeticionesLocal
    print("la moda es: ",moda)

def veinticuatro():
    print("ingrese una lista de números separados por un espacio para ordenarla descendentemente")
    numerosString = input().split()
    numeros = list(map(int, numerosString))
    # algoritmo de selección sobre un mismo arreglo
    # coge un elemento y lo compara contra todos. Escoge el mayor y lo pone en esa posición
    for iAordenar in range(len(numeros)):
        max = numeros[iAordenar]
        maxIndex = 0
        for iAcomparar in range(iAordenar + 1, len(numeros)):
            if numeros[iAcomparar] > max:
                max = numeros[iAcomparar]
                maxIndex = iAcomparar
        if max != numeros[iAordenar]:
            # swap, si es el menor encontrado, se intercambia
            numeros[iAordenar], numeros[maxIndex] = numeros[maxIndex], numeros[iAordenar]
    print(numeros)

def veinticinco():
    print("ingrese una lista de números separados por un espacio para encontrar los múltiplos de 7")
    numerosString = input().split()
    numeros = list(map(int, numerosString))
    multiplosde7 = []
    #si el residuo es 0 al dividirlo por 7, es multiplo
    for x in numeros:
        if x % 7 == 0:
            multiplosde7.append(x)
    print(multiplosde7)


def ventiseis():
    print("ingrese las dimensiones NxM de una matriz separadas por un espacio")
    dimensionesString = input().split()
    print("ingrese un entero para llegar la matriz")
    n = int(input())
    N = int(dimensionesString[0])
    M = int(dimensionesString[1])
    #crea dos listas, la principal (lista de listas) y la que va a ser llenada con n. Una vez se llenen M ns, se agrega la lista 2 a la 1 y

    list1=[]
    list2 = []
    for i in range(N):
        list2 = []
        for i in range(M):
            list2.append(n)
        list1.append(list2)
    print(list1)

#def veintisiete():
