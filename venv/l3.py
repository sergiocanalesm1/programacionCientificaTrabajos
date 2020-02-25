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
    if recorridoNormal != recorridoInverso:
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
def fibonacci(f_x1,f_x2,f_n):
    if f_x1 >= f_n or f_x2 >= f_n:
        return False
    elif f_x1 + f_x2 == f_n:
        return True
    else:
        return fibonacci(f_x2,f_x1 + f_x2,f_n) #el primer valor se convierte en el que estaba de segundo y el segundo se convierte en la suma de los primeros dos
