import numpy as np
import matplotlib.pyplot as plt
import struct as st

def punto1():
    print('ingrese un numero entero positivo para determinar si pertenece a la serie de fibonacci')
    n = int(input())
    if n == 1:
        print(True)
    elif n == 0:
        print(False)
    else:
        print(fibonacci(n))
def fibonacci(numero_usuario,f_x1=1,f_x2=1):#se inicializan en uno si no se especifican
    if f_x1 >= numero_usuario or f_x2 >= numero_usuario:#si la suma ya se pasa, no pertenece a fibonacci
        return False
    elif f_x1 + f_x2 == numero_usuario:
        return True
    else:
        return fibonacci(numero_usuario,f_x2,f_x1 + f_x2) #el primer valor se convierte en el que estaba de segundo y el segundo se convierte en la suma de los primeros dos
def punto2():
    print("ingrese un numero para verificar si pertenece a la serie de numeros cuadrados (1,4,9,16...)")
    x = int(input())
    print(serie_cuadrada(x))
def serie_cuadrada(x,n=1):#el parametro n=1 indica que si solo hay un parametro, n es uno por defecto
    if n ** 2 > x:
        return False
    elif n**2 == x:
        return True
    else:
        return serie_cuadrada(x,n+1)#va entero por entero sacandole el cuadrado para comparar con el numero que metio el usuario

def punto3():
    print("ingrese un x y N separados por un espacio para calcular el valor de la serie de taylor de e**x con N terminos")
    entrada = input().split()
    x = int(entrada[0])
    N = int(entrada[1])
    print(taylor_e(N,x))

def taylor_e(N,x=1,c=0,f=1):
    if c != 0:
        f *= c #para no tener que calcular el factorial cada recursion, solamente se hace de 0 a N y el factorial se va multiplicando por el contador
    if c == N:
        return (x**c)/f
    else:
        return (x**c)/f + taylor_e(N,x,c+1,f)

def punto4():
    print("ingrese un x y n separados por un espacio para calcular el valor de la serie de taylor de sin(x) con n terminos")
    entrada = input().split()
    x = int(entrada[0])
    N = int(entrada[1])
    print(taylor_seno(N,x))
def taylor_seno(N,x=1,c=0,f=1):
    if c != 0:
        f *= 2*c
        f *= 2*c + 1 #las matematicas son bellas: ya se tiene calculado el factorial para n-2, entonces eso solo toca multiplicarlo por n-1 y despues por n
        #aqui me refiero a n como lo que deberia ser el factorial en la ecuacion: (2n+1)!
    if c == N:
        return (((-1)**c)/f) *x**(2*c+1)#ultimo valor
    else:
        return taylor_seno(N,x,c+1,f)+(((-1)**c)/f)*x**(2*c+1)

def punto5():
    print("ingrese un x y n separados por un espacio para calcular el valor de la serie de taylor de cos(x) con n terminos")
    entrada = input().split()
    x = int(entrada[0])
    n = int(entrada[1])
    print(taylor_cos(n,x))
def taylor_cos(N,x=1,c=0,f=1):

    if c!=0:
        f *= 2*c
        f *= 2*c-1# las matematicas son muy bellas: ya se tiene calculado el factorial para n-2, entonces eso solo toca multiplicarlo por n-1 y despues por n
        # aqui me refiero a n como lo que deberia ser el factorial en la ecuacion: (2n)!
    if c == N:
        return (((-1)**c)/f)*x**(2*c)#ultimo valor
    else:
        return taylor_cos(N,x,c+1,f)+(((-1)**c)/f)*x**(2*c)
def punto6():
    print('ingrese un valor x para calcular su error con diferentes N en la serie de taylor de E**x')
    x = int(input())

    n = np.arange(10,1000,10)
    e_values = [taylor_e(N,x) for N in n ]#se le aplica la funcion taylor a cada posicion del arreglo n con el valor x especificado

    plt.figure(1)
    plt.plot(n,e_values)
    plt.title('punto 3')
    plt.show()

    e = np.exp(1)
    error_absoluto = [abs(e-ec) for ec in e_values]#se le saca la magnitud de la diferencia entre lo que yo calcule, y el exp de numpy
    plt.figure(2)
    plt.plot(n, error_absoluto)
    plt.title('error absoluto')
    plt.show()

    error_relativo = [ea/e for ea in error_absoluto]#el cociente entre el error absoluto calculado y el exp calculado por numpy
    plt.figure(3)
    plt.plot(n, error_relativo)
    plt.title('error relativo')
    plt.show()

def punto7():
    print('ingrese un valor x para calcular su error con diferentes N en la serie de taylor de seno')
    x = float(input())

    n = np.arange(10, 1000, 10)
    sin_values = [taylor_seno(N, x) for N in n]  # se le aplica la funcion taylor a cada posicion del arreglo n con el valor x especificado

    plt.figure(1)
    plt.plot(n, sin_values)
    plt.title('punto 4')
    plt.show()

    sin = np.sin(x)

    error_absoluto = [abs(sin - sinc) for sinc in sin_values]  # se le saca la magnitud de la diferencia entre lo que yo calcule, y el sin de numpy
    plt.figure(2)
    plt.ylim(-0.1, 0.1)
    plt.plot(n, error_absoluto)
    plt.title('error absoluto')
    plt.show()

    error_relativo = [ea / sin for ea in error_absoluto]  # el cociente entre el error absoluto calculado y el sin calculado por numpy
    plt.figure(3)
    plt.plot(n, error_relativo)
    plt.ylim(-0.1, 0.1)
    plt.title('error relativo')
    plt.show()

def punto8():
    print('ingrese un valor x para calcular su error con diferentes N en la serie de taylor de coseno')
    x = float(input())

    n = np.arange(10, 1000, 10)
    cos_values = [taylor_cos(N, x) for N in n]  # se le aplica la funcion taylor a cada posicion del arreglo n con el valor x especificado

    plt.figure(1)
    plt.plot(n, cos_values)
    plt.title('punto 5')
    plt.show()

    cos = np.cos(x)
    error_absoluto = [abs(cos - cosc) for cosc in cos_values]  # se le saca la magnitud de la diferencia entre lo que yo calcule, y el cos de numpy
    plt.figure(2)
    plt.ylim(-0.1, 0.1)
    plt.plot(n, error_absoluto)
    plt.title('error absoluto')
    plt.show()

    error_relativo = [ea / cos for ea in error_absoluto]  # el cociente entre el error absoluto calculado y el cos calculado por numpy
    plt.figure(3)
    plt.ylim(-0.1, 0.1)
    plt.plot(n, error_relativo)
    plt.title('error relativo')
    plt.show()

punto7()
punto8()
def punto9():
    arreglo = np.random.randint(-10,10,1000)
    name = "FileBinInt16.bin"
    f = open(name,"wb")
    paquete = st.pack("h"*len(arreglo),*arreglo)
    f.write(paquete)

def punto10():
    f = open("FileBinInt16.bin","rb")
    file = f.read()
    pack = st.unpack("h"*int(len(file)/2),file)
    plt.figure()
    plt.hist(pack,bins=30,density=True)
    plt.show()
    f.close()
def punto11():
    f = open("FileBinDouble.bin","wb")
    a = 2*np.random.random_sample(1000)-1
    pack = st.pack("d"*len(a),*a)
    f.write(pack)
    f.close()
def punto12():
    f = open("FileBinDouble.bin","rb")
    file = f.read()
    pack = st.unpack("d"*int(len(file)/8),file)
    plt.figure()
    plt.hist(pack,bins=30,density=True)
    plt.show()
    f.close()

def punto13(imprimir=True):#para no tener que imprimir en el punto 14
    f = open("File-214.bin","rb")
    file = f.read()
    arreglo_leido = st.unpack("I" * int(len(file) / 4),file)
    if imprimir:
        print(np.mean(arreglo_leido))
    f.close()
    return arreglo_leido
def punto14():
    print([fibonacci(x) for x in punto13(False)].count(True)) #se crea una lista booleana con los número que pertencen a la serie fib e iimprime los true
def punto15():
    print([serie_cuadrada(x) for x in punto13(False)].count(True))#lo mismo del punto14




