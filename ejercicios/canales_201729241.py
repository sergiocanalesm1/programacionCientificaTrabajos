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
##
import scipy.optimize as opt
import numpy as np
def f1(x):
    return - (np.sqrt(3*x)**(2/5))+x**3*np.cos(3*x)+4*x**2 - 7
def biseccion(f,tol):
    x0 = 1.0
    x1 = 2.0
    tolx = tol
    tolf = tolx
    x2prev = x1
    iteraciones = 0
    r_candidatas = np.array([])
    while True:
        iteraciones += 1
        x2 = (x0+x1)/2.0
        r_candidatas = np.append(r_candidatas,x2)
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        if f(x2)*f(x0) < 0:
            x1=x2
        else:
            x0 = x2
        x2prev = x2
    r_verdadero = opt.fsolve(f1,x1)
    error_estimado = np.abs(r_candidatas-r_verdadero)
    tam = np.size(error_estimado)
    tasas_convergencias = (np.log10(error_estimado[1:tam-1] / error_estimado[2:tam]) /np.log10(error_estimado[0:tam-2] / error_estimado[1:tam-1]))
    print("Biseccion: con {} iteraciones, {} de tolerancia, la raiz es: {} y tasa de convergencia entre {} y {} ".format(iteraciones,tolx,x2,tasas_convergencias[-2],tasas_convergencias[-1]))
print("F1")
biseccion(f1,10**-10)
#print("F2")
#falsapos(f2,10**-5)
#falsapos(f2,10**-10)
#biseccion(f2,10**-10)

##punto fijo
import numpy as np

#g(x) candidatas para f1
def gf11(x):
    return np.sqrt((1.0/4.0)*((np.sqrt(3*x))**(2.0/5.0)-x**3*np.cos(3*x)+7))
def gf12(x):
    return (((np.sqrt(3.0*x)**(2.0/5.0))-4.0*(x**2.0)-7.0)/np.cos(3.0*x))**(3.0)
def gf13(x):
    return - (np.sqrt(3*x)**(2/5))+x**3*np.cos(3*x)+4*x**2 - 7 + x


#g(x) candidatas para f2
def gf21(x):
    return (x**0.25-np.sin(3.5*x)-4.0*x**0.5+5)/2
def gf22(x):
    return (-np.sin(3.5*x)-4*x**(0.5)+2*x + 5)**4.0

def puntofijo(f,tol,g):
    diverge = False
    x1=2.0
    tolx = tol
    tolf = tolx
    x2prev = x1
    iteraciones = 0
    while True:
        iteraciones +=1
        if iteraciones > 100:
            diverge = True
            print("la función diverge probando con {} iteraciones".format(iteraciones))
            break
        x2 = g(x1)
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        x1=x2
        x2prev=x2

    if not diverge:
        print("Punto fijo: con {} iteraciones, {} de tolerancia, la raiz es: {}".format(iteraciones,tolx,x2))

'''
print("f1\n")
print("g(x) candidata np.sqrt((1.0/4.0)*((np.sqrt(3*x))**(2.0/5.0)-x**3*np.cos(3*x)+7))")
puntofijo(f1,10**-10,gf11)
puntofijo(f1,10**-15,gf11)

print("g(x) candidata (((np.sqrt(3.0*x)**(2.0/5.0))-4.0*(x**2.0)-7.0)/np.cos(3.0*x))**(3.0)")
puntofijo(f1,10**-5,gf12)
print("g(x) candidata - (np.sqrt(3*x)**(2/5))+x**3*np.cos(3*x)+4*x**2 - 7 + x")
puntofijo(f1,10**-5,gf13)

print("\nf2")
print("g(x) candidata (x**0.25-np.sin(3.5*x)-4.0*x**0.5+5)/2")
puntofijo(f2,10**-5,gf21)
print("g(x) candidata (-np.sin(3.5*x)-4*x**(0.5)+2*x + 5)**4.0" )
puntofijo(f2,10**-5,gf22)
'''
##syms newton
import numpy as np
import sympy as sym
import scipy.optimize as opt
def funcion1(x):
    return - (np.sqrt(3*x)**(2/5))+x**3*np.cos(3*x)+4*x**2 - 7
def newton(f, tol, df):
    x1 = 2.0
    tolx = tol
    tolf = tolx
    x2prev = x1
    iteraciones = 0
    r_candidatas = np.array([])
    while True:
        iteraciones += 1
        x2 = x1 - (f.subs(xx,x1) / df.subs(xx,x1))
        r_candidatas = np.append(r_candidatas, x2)
        if np.abs(x2 - x2prev) <= tolx:
            break
        if np.abs(f.subs(xx,x2)) <= tolf:
            break
        x1 = x2
        x2prev = x2
    r_verdadero = opt.fsolve(funcion1, x1)
    error_estimado = np.abs(r_candidatas - r_verdadero)
    tam = np.size(error_estimado)
    tasas_convergencias = (np.log10(error_estimado[1:tam - 1] / error_estimado[2:tam]) / np.log10(
        error_estimado[0:tam - 2] / error_estimado[1:tam - 1]))
    print("Newton: con {} iteraciones, {} de tolerancia, la raiz es: {} y tasa de convergencia entre {} y {} ".format(iteraciones, tolx, x2, tasas_convergencias[-2], tasas_convergencias[-1]))


xx = sym.Symbol("xx")
f1 = -(sym.sqrt(3.0*xx)**(2.0/5.0))+xx**3.0*sym.cos(3.0*xx)+4.0*xx**2.0 - 7.0
df1 = f1.diff()

f2 = -xx**(0.25)+sym.sin(3.5*xx)+4*xx**(0.5)+2*xx - 5
df2 = f2.diff()
print('para F1')
newton(f1,10**-15,df1)
'''
print('para F1')
newton(f1,10**-15,df1)

print('para F2')
newton(f2,10**-5,df2)
newton(f2,10**-15,df2)


'''
## newton-rhapson sin syms
import numpy as np

import scipy.optimize as opt

def f1(x):
    return - (np.sqrt(3.0*x)**(2.0/5.0))+x**3.0*np.cos(3.0*x)+4.0*x**2.0 - 7.0
def df1(x):
    return (-3**(1.0/5.0)/5)*x**(-4.0/5.0)-3.0*x**3.0*np.sin(3.0*x)+3.0*x**2.0*np.cos(3.0*x)+8.0*x


def newton(f,tol,df):
    x1=2.0
    tolx=tol
    tolf=tolx
    x2prev=x1
    iteraciones=0
    r_candidatas = np.array([])
    while True:
        iteraciones += 1
        x2=x1-(f(x1)/df(x1))
        r_candidatas = np.append(r_candidatas, x2)
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        x1 = x2
        x2prev = x2
    r_verdadero = opt.fsolve(f1, x1)
    error_estimado = np.abs(r_candidatas - r_verdadero)
    tam = np.size(error_estimado)
    tasas_convergencias = (np.log10(error_estimado[1:tam - 1] / error_estimado[2:tam]) / np.log10(
        error_estimado[0:tam - 2] / error_estimado[1:tam - 1]))
    print("Newton: con {} iteraciones, {} de tolerancia, la raiz es: {} y tasa de convergencia entre {} y {} ".format(iteraciones, tolx, x2, tasas_convergencias[-2], tasas_convergencias[-1]))

newton(f1,10**-5,df1)
#newton(f1,10**-15,df1)
#newton(f2,10**-5,df2)
#newton(f2,10**-15,df2)


## secante
import numpy as np
import scipy.optimize as opt
def funcion1(x):
    return - (np.sqrt(3.0*x)**(2.0/5.0))+(x**3.0)*np.cos(3.0*x)+4.0*(x**2.0) - 7.0
def funcion2(x):
    return -x**(0.25)+np.sin(3.5*x)+4*x**(0.5)+2*x - 5
def secante(f,tol):
    x0 = 2.0
    x1 = 1.9
    tolf = tol
    tolx = tolf
    x2prev = x1
    r_candidatas = np.array([])
    iteraciones = 0
    while True:
        iteraciones +=1
        x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))
        r_candidatas = np.append(r_candidatas, x2)
        if np.abs(x2 - x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        x0 = x1
        x1 = x2
        x2prev = x2
    r_verdadero = opt.fsolve(funcion1, x1)
    error_estimado = np.abs(r_candidatas - r_verdadero)
    tam = np.size(error_estimado)
    tasas_convergencias = (np.log10(error_estimado[1:tam - 1] / error_estimado[2:tam]) / np.log10(
        error_estimado[0:tam - 2] / error_estimado[1:tam - 1]))
    print("Secante: con {} iteraciones, {} de tolerancia, la raiz es: {} y tasa de convergencia entre {} y {} ".format(iteraciones, tolx, x2, tasas_convergencias[-2], tasas_convergencias[-1]))

print("f1")
secante(funcion1,10**-15)
print("f2")
secante(funcion2,10**-5)
secante(funcion2,10**-15)


