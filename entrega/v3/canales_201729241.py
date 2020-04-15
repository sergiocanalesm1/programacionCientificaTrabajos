##punto fijo
import numpy as np
def f1(x):
    return - (np.sqrt(3.0*x)**(2.0/5.0))+x**3.0*np.cos(3.0*x)+4.0*x**2.0 - 7.0

#g(x) candidatas para f1
def gf11(x):
    return np.sqrt((1.0/4.0)*((np.sqrt(3*x))**(2.0/5.0)-x**3*np.cos(3*x)+7))
def gf12(x):
    return (((np.sqrt(3.0*x)**(2.0/5.0))-4.0*(x**2.0)-7.0)/np.cos(3.0*x))**(3.0)
def gf13(x):
    return - (np.sqrt(3*x)**(2/5))+x**3*np.cos(3*x)+4*x**2 - 7 + x

def f2(x):
    return -x**(0.25)+np.sin(3.5*x)+4*x**(0.5)+2*x - 5
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

##syms newton
import numpy as np
import sympy as sym

def newton(f, tol, df):
    x1 = 2.0
    tolx = tol
    tolf = tolx
    x2prev = x1
    iteraciones = 0
    while True:
        iteraciones += 1
        x2 = x1 - (f.subs(xx,x1) / df.subs(xx,x1))
        if np.abs(x2 - x2prev) <= tolx:
            break
        if np.abs(f.subs(xx,x2)) <= tolf:
            break
        x1 = x2
        x2prev = x2
    print("Newton: con {} iteraciones, {} de tolerancia, la raiz es: {}".format(iteraciones, tolx, x2))


xx = sym.Symbol("xx")
f1 = -(sym.sqrt(3.0*xx)**(2.0/5.0))+xx**3.0*sym.cos(3.0*xx)+4.0*xx**2.0 - 7.0
df1 = f1.diff()

f2 = -xx**(0.25)+sym.sin(3.5*xx)+4*xx**(0.5)+2*xx - 5
df2 = f2.diff()

print('para F1')
newton(f1,10**-15,df1)

print('para F2')
newton(f2,10**-5,df2)
newton(f2,10**-15,df2)