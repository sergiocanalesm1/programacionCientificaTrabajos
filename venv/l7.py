import numpy as np
import sympy as sym
import scipy.optimize as opt


#biseccion
def biseccion(f,tolx=10**-5,tolf=10**-5,x0=1.0,x1=2.0):

    x2prev = x1
    iteraciones = 0
    r_candidatas = []
    while True:
        iteraciones += 1
        x2 = (x0+x1)/2.0
        r_candidatas.append(x2)
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f.subs(x,x2)) <= tolf:
            break
        if f.subs(x,x2)*f.subs(x,x0) < 0:
            x1=x2
        else:
            x0 = x2
        x2prev = x2

    return r_candidatas

#falsa posicion
def falsapos(f,tolx=10**-5,tolf=10**-5,x0=1.0,x1=2.0):

    x2prev = x1
    iteraciones = 0
    r_candidatas = []

    while True:
        iteraciones+=1
        x2 = x1 - (f.subs(x,x1)*(x1-x0)/(f.subs(x,x1)-f.subs(x,x0)))
        r_candidatas.append(x2)
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f.subs(x,x2)) <= tolf:
            break
        if f.subs(x,x2)*f.subs(x,x0) < 0:
            x1=x2
        else:
            x0 = x2
        x2prev = x2

    return r_candidatas
#punto fijo
def puntofijo(f,g,tolx=10**-5,tolf=10**-5,x0=0,x1=2.0):
    #diverge = False

    x2prev = x1
    iteraciones = 0
    r_candidatas = []

    while True:
        iteraciones +=1
        if iteraciones > 100:
            #diverge = True
            r_candidatas = []#diverge
            break
        x2 = g.subs(x,x1)
        r_candidatas.append(x2)
        if np.abs(x2-x2prev) <= tolx:
            break
        if np.abs(f.subs(x,x2)) <= tolf:
            break
        x1=x2
        x2prev=x2

    return r_candidatas

#newton
def newton(f,tolx=10**-5,tolf=10**-5,x0=0,x1=2.0):

    x2prev = x1
    iteraciones = 0
    r_candidatas = []
    df = f.diff()
    while True:
        iteraciones += 1
        x2 = x1 - (f.subs(x,x1) / df.subs(x,x1))
        r_candidatas.append(x2)
        if np.abs(x2 - x2prev) <= tolx:
            break
        if np.abs(f.subs(x,x2)) <= tolf:
            break
        x1 = x2
        x2prev = x2
        #print(x2)
        #print(iteraciones)
    return r_candidatas




#secante
def secante(f,tolx=10**-5,tolf=10**-5,x0=2.0,x1=1.0):

    x2prev = x1
    iteraciones = 0
    r_candidatas = []

    while True:
        iteraciones +=1
        x2 = x1 - (f.subs(x,x1) * (x1 - x0) / (f.subs(x,x1) - f.subs(x,x0)))
        r_candidatas.append(x2)
        if np.abs(x2 - x2prev) <= tolx:
            break
        if np.abs(f.subs(x,x2)) <= tolf:
            break
        x0 = x1
        x1 = x2
        x2prev = x2
    return r_candidatas

def tasa_convergencia(r_candidatas,funcion,x):
    r_verdadero = opt.fsolve(funcion, x)
    error_estimado = np.abs(r_candidatas - r_verdadero)
    tam = np.size(error_estimado)
    tasas_convergencias = (np.log10(error_estimado[1:tam - 1] / error_estimado[2:tam]) / np.log10(
        error_estimado[0:tam - 2] / error_estimado[1:tam - 1]))
    return tasas_convergencias[2:-1]

x = sym.Symbol("x")
#f1 = -(sym.sqrt(3.0*x)**(2.0/5.0))+x**3.0*sym.cos(3.0*x)+4.0*x**2.0 - 7.0
#f2 = -x**(0.25)+sym.sin(3.5*x)+4*x**(0.5)+2*x - 5
def tabla(metodo,funcion,x0,x1):
    raices = metodo(funcion, x0=x0, x1=x1)
    return (len(raices),raices[-1],funcion.subs(x, raices[-1]))#tupla con iteraciones, raiz y valor de raiz

#i)
fi = sym.exp(-5*x**2)-x**(3.0/4.0)+sym.sin(4*x)-1

filaIBiseccion = tabla(biseccion,fi,0.2,0.6)
filaIFalsaPos = 0
    #tabla(falsapos,fi,0.2,0.6)
filaINewton = tabla(newton,fi,0,0.6)#no se usa el 0
filaISecante = tabla(secante,fi,0.55,0.6)
i = (filaIBiseccion,filaIFalsaPos, filaINewton,filaISecante)
print(i)

#ii)
fii = sym.sin(4*x)*x+x**5+6*x-4

filaIIBiseccion = tabla(biseccion,fii,0.0,1.0)
filaIIFalsaPos = 0
    #tabla(falsapos,fii,0.0,1.0)
filaIINewton = tabla(newton,fii,0,1.0)#no se usa el 0
filaIISecante = tabla(secante,fii,0.95,1.0)#me invente el 0.95
ii = (filaIIBiseccion,filaIIFalsaPos,filaIINewton,filaIISecante)
print(ii)

#iii)
fiii = -3.65*sym.ln(x/5.33)+sym.sqrt(2)*sym.exp(-(sym.pi/2)**2-4.25)+10.24*sym.cos(x-2.2)-6.67*(sym.pi/2)

filaIIIBiseccion = tabla(biseccion,fiii,0.01,0.1)
filaIIIFalsaPos = 0#tabla(falsapos,fiii,0.01,0.1)
filaIIINewton = tabla(newton,fiii,0,0.01)#no se usa el 0 ******* no funciona
filaIIISecante = tabla(secante,fiii,0.01,0.015) #no funciona
iii = (filaIIIBiseccion,filaIIIFalsaPos,filaIIINewton,filaIIISecante)
print(iii)

