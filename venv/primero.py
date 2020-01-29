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
    if numeros[1] == numeros[2] == numeros[3]:
        print(0)
    else:
        print(sum(numeros))


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
    print("ingrese dos puntos cardinales en el siguiente formato: x1 y1 x2 y2")
    numerosString = input().split()
    numeros = list(map(int, numerosString))
    #se utiliza la ecuación
    distanciaEuclidiana = ((numeros[3]-numeros[1])**2+(numeros[2]-numeros[0])**2)**(1/2)
    print("la distancia euclidiana entre {} y {}, es: {}".format(numeros[0:2],numeros[2:],distanciaEuclidiana))


# uno()
# dos()
# tres()
#cuatro()
# cinco()
# seis()
# siete()
# ocho()
# nueve()
#diez()
# once()
# doce()
#trece()
catorce()