'''
    Programación Científica
    Parcial 3
    Sergio Canales
    201729241
    Ingeniería de sistemas y computación
'''
# no alcancé a pasarlo bien a pdf, en el .txt se ve mejor el punto de la tabla

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import struct as st
from fpdf import FPDF


#def f(r1,z):
#    return ((r1 / 0.00055)**2)*np.log((r1 / 0.00055)**2)+371.0930*((r1 / 0.00055)**2)*12800.0*(((r1 / 0.00055)**2)-1)*z-2874.3785

def fs(z):
    return (y**2)*sym.log(y**2)+371.0930*(y**2)*12800.0*((y**2)-1)*z-2874.3785

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

def tabla(metodo,f,x0,x1):
    raices = metodo(f, x0=x0, x1=x1,tolx=10**-5,tolf=10**-5)
    f = sym.lambdify([x], f, "numpy")
    return [len(raices),f(raices[-1]),raices[-1]]

def punto1a():

    for zi in z:
       plt.figure(zi)
       fi = fs(zi)
       r_vals = np.arange(0.5,12,0.001)
       f_e= sym.lambdify([x],fi,"numpy")
       y_vals = f_e(r_vals)
       plt.plot(r_vals,y_vals)
       plt.show()



def punto1b():
    a = open("tabla.txt","w")
    #a.write("\r z \t \t iteraciones \t y \t rcrit \n \n")
    a.write("\t \t|Bi | New | FP \t || \tBiseccion \t \t    | \t Newton    | \t Falsa Pos \t ||   Biseccion \t   |  Newton  |  Falsa Pos \n")
    for zi in z:
        b = tabla(biseccion, fs(zi),1.0,12.0)
        n =  tabla(newton, fs(zi),0,12.0)
        fp = tabla(falsapos,fs(zi),1.0,3.0)

        a.write(" {} ".format(round(zi,3)))

        a.write("  {} ".format(round(b[0],10)))
        a.write("  {} ".format(round(n[0],10)))
        a.write("  {} ||".format(round(fp[0],10)))

        a.write("  {} ".format(round(b[1], 10)))
        a.write("  {} ".format(round(n[1], 10)))
        a.write("  {} ||".format(round(fp[1], 10)))

        a.write("  {} ".format(round(b[2], 10)))
        a.write("  {} ".format(round(n[2], 10)))
        a.write("  {} ".format(round(fp[2], 10)))

        a.write("\n")

    a.close()

def punto1c():
    for zi in z:
        b = tabla(biseccion, fs(zi),1.0,12.0)
        n =  tabla(newton, fs(zi),0,12.0)
        fp = tabla(falsapos,fs(zi),1.0,3.0)

        plt.figure(zi)
        fi = fs(zi)
        r_vals = np.arange(0.5, 12, 0.001)
        f_e = sym.lambdify([x], fi, "numpy")
        y_vals = f_e(r_vals)
        plt.plot(r_vals, y_vals)
        plt.plot(b[2],b[1],".g",label="biseccion")
        plt.plot(n[2], n[1],".r",label="newton")
        plt.plot(fp[2], fp[1],".b",label="falsapos")
        plt.legend(loc='upper left')
        plt.show()
def converttoPDf():
    #https://www.geeksforgeeks.org/convert-text-and-text-file-to-pdf-using-python/
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    f = open("tabla.txt","r")
    for x in f:
        pdf.cell(400, 20, txt=x, ln=1)
    pdf.output("B.pdf")
    f.close()

z = np.arange(0.001,0.111,0.01)
x = sym.Symbol("x")
y = x/0.00055


#punto1a()
#punto1b()
#punto1c()

#converttoPDf()
#bono
def regresion(x,y):
    x = np.array(list(x))#pasar las tuplas a listas y luego a arreglos de numpy
    y = np.array(list(y))
    meanX = np.mean(x)
    meanY = np.mean(y)
    N = np.size(x)

    A = np.array([[1, meanX], [meanX, np.sum(x ** 2) / N]])
    b = np.array([[meanY], [np.sum(x * y) / N]])

    return np.linalg.solve(A,b)
def bono():
    f = open("Parcial-03-P02-X.bin","rb")
    ar = f.read()
    X = st.unpack("d" * int(len(ar) / 8), ar)
    f.close()

    f = open("Parcial-03-P02-Y.bin", "rb")
    ar = f.read()
    Y = st.unpack("d" * int(len(ar) / 8), ar)
    f.close()

    sol = regresion(X,Y)
    print("el valor del coeficiente a_0 es: {} y el coeficiente de a_1 es: {}".format(sol[1],sol[0]))
#bono()
