##
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return - (np.sqrt(3*x)**(2/5))+x**3*np.cos(3*x)+4*x**2 - 7
def f2(x):
    return -x**(0.25)+np.sin(3.5*x)+4*x**(0.5)+2*x - 5
def falsapos(f,tol):
    x0 = 1.0
    x1 = 2.0
    tolx = tol
    tolf = tolx
    x2prev = x1
    iteraciones = 0
    while True:
        iteraciones+=1
        x2 = x1 - (f(x1)*(x1-x0)/(f(x1)-f(x0)))
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        if f(x2)*f(x0) < 0:
            x1=x2
        else:
            x0 = x2
        x2prev = x2
    print("Falsa posicion: con {} iteraciones, {} de tolerancia, la raiz es: {}".format(iteraciones,tolx,x2))
def biseccion(f,tol):
    x0 = 1.0
    x1 = 2.0
    tolx = tol
    tolf = tolx
    x2prev = x1
    iteraciones = 0
    while True:
        iteraciones += 1
        x2 = (x0+x1)/2.0
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        if f(x2)*f(x0) < 0:
            x1=x2
        else:
            x0 = x2
        x2prev = x2
    print("Biseccion: con {} iteraciones, {} de tolerancia, la raiz es: {}".format(iteraciones,tolx,x2))
print("F1")
falsapos(f1,10**-5)
falsapos(f1,10**-10)
#biseccion(f1,10**-10)
print("F2")
falsapos(f2,10**-5)
falsapos(f2,10**-10)
#biseccion(f2,10**-10)

##punto fijo
import numpy as np
def f1(x):
    return - (np.sqrt(3*x)**(2/5))+x**3*np.cos(3*x)+4*x**2 - 7
def f2(x):
    return -x**(0.25)+np.sin(3.5*x)+4*x**(0.5)+2*x - 5
def g(f,x):
    #return x + (np.sqrt(3*x))**(2/5)-x**3*np.cos(3*x)-4*x**2+7
    return np.sqrt((1.0/4.0)*((np.sqrt(3*x))**(2.0/5.0)-x**3*np.cos(3*x)+7))
def puntofijo(f,tol):
    x1=2.0
    tolx = tol
    tolf = tolx
    x2prev = x1
    iteraciones = 0
    while True:
        iteraciones +=1
        x2 = g(f,x1)
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        x1=x2
        x2prev=x2
    print("Punto fijo: con {} iteraciones, {} de tolerancia, la raiz es: {}".format(iteraciones,tolx,x2))

puntofijo(f1,10**-5)
puntofijo(f1,10**-10)