'''
    Programación Científica
    Laboratorio 7
    Sergio Canales
    201729241
    Ingeniería de sistemas y computación
'''


import numpy as np
import sympy as sym
import scipy.optimize as opt
import matplotlib.pyplot as plt

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

def puntofijo(f,g,tolx=10**-5,tolf=10**-5,x1=2.0):
    #diverge = False
    f = sym.lambdify([x], f, "numpy")
    g = sym.lambdify([x],g,"numpy")
    x2prev = x1
    iteraciones = 0
    r_candidatas = []

    while True:
        iteraciones +=1
        if iteraciones > 100:
            #diverge = True
            r_candidatas = []#diverge
            break
        x2 = g(x1)
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

def tasa_convergencia(r_candidatas,fun,x1=2):
    f = sym.lambdify([x],fun,"numpy")
    r_verdadero = opt.fsolve(f, x1)
    error_estimado = np.abs(r_candidatas - r_verdadero)
    tam = np.size(error_estimado)
    tasas_convergencias = (np.log10(error_estimado[1:tam - 1] / error_estimado[2:tam]) / np.log10(
        error_estimado[0:tam - 2] / error_estimado[1:tam - 1]))
    return tasas_convergencias


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

def intervalos():
    prop = -1.440*x**(-2)+0.710*x**(-1)+0.688+0.0636*x-(3.0/5.0)
    prop_e = sym.lambdify([x],prop,"numpy")
    plt.figure()
    domain = np.arange(0,3,0.5)
    plt.plot(domain,prop_e(domain))
    plt.grid(True)
    plt.show()

def prueba_puntofijo():
    prop = -1.440 * x ** (-2) + 0.710 * x ** (-1) + 0.688 + 0.0636 * x - (3.0 / 5.0)
    i = ((1.0/1.440)*(0.710*x**(-1)+0.0636*x+0.088))**(-1.0/2.0)
    ii = (1.0/0.0636)*(-0.710*x**(-1)+1.440*x**(-2)*x-0.088)
    iii = 1.440*x**(-2)-0.710*x**(-1)-0.0636*x-0.088+x

    i_e = sym.lambdify([x],i,"numpy")
    ii_e = sym.lambdify([x], ii, "numpy")
    iii_e = sym.lambdify([x], iii, "numpy")
    a = open("prueba_puntofijo.txt","w")
    intervalo = np.arange(1,1.5,0.1)
    gs =[i,ii,iii]
    gse = [i_e,ii_e,iii_e]

    for _ in range(3):
        a.write("Expresion {}\n".format((_+1)*"i"))
        a.write("Iter \t nr \t \t g(nr) \t \t \t \t raiz \n")
        r = puntofijo(prop,gs[_], x1=2.0)
        a.write("{}         {}      {}   {}\n".format(0,2,round(gse[_](2.0),10),0))
        a.write("{}         {}      {}   {}\n".format(3, 2, round(gse[_](2),10), np.abs(r[0] - r[3])))
        a.write("{}         {}      {}   {}\n".format(5, 2, round(gse[_](2),10), np.abs(r[3] - r[5])))
        a.write("{}        {}      {}   {}\n".format(10, 2, round(gse[_](2),10), np.abs(r[5] - r[-1])))
        a.write("{}        {}      {}   {}\n\n\n".format(13, 2, round(gse[_](2), 10), np.abs(r[-2] - r[-1])))


    a.close()

def prueba_newton():
    prop = -1.440 * x ** (-2) + 0.710 * x ** (-1) + 0.688 + 0.0636 * x - (3.0 / 5.0)
    a= open("prueba_newton.txt","w")
    p_e = sym.lambdify([x],prop,"numpy")

    a.write("Iter \t nr \t \t g(nr) \t \t \t \t raiz \n")
    r = newton(prop, x1=2.0)
    a.write("{}         {}        {}     {}\n".format(0, 2, round(p_e(2.0), 10), 0))
    a.write("{}         {}        {}     {}\n".format(3, 2, round(p_e(2), 10), np.abs(r[0] - r[3])))
    a.write("{}         {}        {}     {}\n".format(5, 2, round(p_e(2), 10), np.abs(r[3] - r[-1])))
    a.write("{}        {}        {}     {}\n".format(10, 2, round(p_e(2), 10), np.abs(r[-2] - r[-1])))

    a.close()
def tasa_convergencia_newton():
    prop = -1.440 * x ** (-2) + 0.710 * x ** (-1) + 0.688 + 0.0636 * x - (3.0 / 5.0)
    #p_e = sym.lambdify([x], prop, "numpy")
    r = newton(prop, x1=2.0)
    tasa = tasa_convergencia(r,prop,x1=2.0)
    print(tasa[-1])

llenar_tabla()
intervalos()
prueba_puntofijo()
prueba_newton()
tasa_convergencia_newton()