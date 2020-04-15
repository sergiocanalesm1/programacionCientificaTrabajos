import numpy as np
import sympy as sym
import scipy.optimize as opt


x = sym.Symbol("x")

def biseccion(f,tolx=10**-5,tolf=10**-5,x0=1.0,x1=2.0):
    f = sym.lambdify([x], f, "numpy")
    x2prev = x1
    iteraciones = 0
    r_candidatas = []
    while True:
        iteraciones += 1
        x2 = (x0+x1)/2.0
        r_candidatas.append(x2)
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        if f(x2)*f(x0) < 0:
            x1=x2
        else:
            x0 = x2
        x2prev = x2

    return r_candidatas


def falsapos(f,tolx=10**-5,tolf=10**-5,x0=1.0,x1=2.0):
    f = sym.lambdify([x], f, "numpy")
    x2prev = x1
    iteraciones = 0
    r_candidatas = []

    while True:
        iteraciones+=1
        x2 = x1 - (f(x1)*(x1-x0)/(f(x1)-f(x0)))
        r_candidatas.append(x2)
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        if f(x2)*f(x0) < 0:
            x1=x2
        else:
            x0 = x2
        x2prev = x2

    return r_candidatas

def puntofijo(f,g,tolx=10**-5,tolf=10**-5,x0=0,x1=2.0):
    #diverge = False
    f = sym.lambdify([x], f, "numpy")
    x2prev = x1
    iteraciones = 0
    r_candidatas = []

    while True:
        iteraciones +=1
        if iteraciones > 100:
            #diverge = True
            r_candidatas = []#diverge
            break
        x2 = g(x,x1)
        r_candidatas.append(x2)
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        x1=x2
        x2prev=x2

    return r_candidatas


def newton(f,tolx=10**-5,tolf=10**-5,x0=0,x1=2.0):

    x2prev = x1
    iteraciones = 0
    r_candidatas = []
    df = sym.lambdify([x],f.diff(x),"numpy")
    f = sym.lambdify([x], f, "numpy")
    while True:
        iteraciones += 1
        x2 = x1 - (f(x1) / df(x1))
        r_candidatas.append(x2)
        if np.abs(x2 - x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        x1 = x2
        x2prev = x2
    return r_candidatas



#secante
def secante(f,tolx=10**-5,tolf=10**-5,x0=2.0,x1=1.0):
    f = sym.lambdify([x], f, "numpy")
    x2prev = x1
    iteraciones = 0
    r_candidatas = []

    while True:
        iteraciones +=1
        x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))
        r_candidatas.append(x2)
        if np.abs(x2 - x2prev) <= tolx:
            break
        if np.abs(f(x2)) <= tolf:
            break
        x0 = x1
        x1 = x2
        x2prev = x2
    return r_candidatas

def tasa_convergencia(r_candidatas,fun,x):
    f = sym.lambdify([x],fun,"numpy")
    r_verdadero = opt.fsolve(f, x)
    error_estimado = np.abs(r_candidatas - r_verdadero)
    tam = np.size(error_estimado)
    tasas_convergencias = (np.log10(error_estimado[1:tam - 1] / error_estimado[2:tam]) / np.log10(
        error_estimado[0:tam - 2] / error_estimado[1:tam - 1]))
    return tasas_convergencias[2:-1]


#f1 = -(sym.sqrt(3.0*x)**(2.0/5.0))+x**3.0*sym.cos(3.0*x)+4.0*x**2.0 - 7.0
#f2 = -x**(0.25)+sym.sin(3.5*x)+4*x**(0.5)+2*x - 5

def tabla(metodo,f,x0,x1):
    raices = metodo(f, x0=x0, x1=x1)
    f = sym.lambdify([x], f, "numpy")
    return (len(raices),raices[-1],f(raices[-1]))#tupla con iteraciones, raiz y valor de raiz



def llenar_tabla():
    a = open("tabla.txt","w")
    a.write("\t \t \t \t iteraciones \t raiz \t f(raiz) \n \n")

    #i)
    fi = sym.exp(-5 * x ** 2) - x ** (3.0 / 4.0) + sym.sin(4 * x) - 1
    a.write("i) {}\n".format(fi))
    a.write("Biseccion:      {} \n".format(tabla(biseccion,fi,0.2,0.6)))
    a.write("falsa posicion: {} \n".format(tabla(falsapos,fi,0.2,0.6)))
    a.write("Newton:         {} \n".format(tabla(newton,fi,0,0.6)))
    a.write("Secante:        {} \n".format(tabla(secante,fi,0.55,0.6)))
    a.write("\n")

    #ii)
    fii = sym.sin(4*x)*x+x**5+6*x-4
    a.write("ii) {}\n".format(fii))
    a.write("Biseccion:      {} \n".format(tabla(biseccion,fii,0.0,1.0)))
    a.write("falsa posicion: {} \n".format(tabla(falsapos,fii,0.0,1.0)))
    a.write("Newton:         {} \n".format(tabla(newton,fii,0,1.0)))
    a.write("Secante:        {} \n".format(tabla(secante,fii,0.95,1.0)))
    a.write("\n")

    #iii)
    fiii = -3.65*sym.ln(x/5.33)+sym.sqrt(2)*sym.exp(-(sym.pi/2)**2-4.25)+10.24*sym.cos(x-2.2)-6.67*(sym.pi/2)
    a.write("iii) {}\n".format(fiii))
    a.write("Biseccion:      {} \n".format(tabla(biseccion,fiii,0.01,0.1)))
    a.write("falsa posicion: {} \n".format(tabla(falsapos,fiii,0.01,0.1)))
    a.write("Newton:         {} \n".format(tabla(newton,fiii,0,0.01)))
    a.write("Secante:        {} \n".format(tabla(secante,fiii,0.01,0.015)))
    a.write("\n")

    a.close()

