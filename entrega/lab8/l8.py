import numpy as np
import sympy as sym
import scipy.optimize as opt
import matplotlib.pyplot as plt


def derivadas_parciales(fi,fii):
    return sym.lambdify([x1,x2],fi.diff(x1),"numpy"),sym.lambdify([x1,x2],fi.diff(x2),"numpy"),sym.lambdify([x1,x2],fii.diff(x1),"numpy"),sym.lambdify([x1,x2],fii.diff(x2),"numpy")
def evaluar(fi,fii):
    return sym.lambdify([x1,x2],fi,"numpy"),sym.lambdify([x1,x2],fii,"numpy")


def jaco(a,b,fi,fii):
    dfix1, dfix2, dfiix1, dfiix2 = derivadas_parciales(fi, fii)
    jac = np.zeros([2,2])
    jac[0,0] = dfix1(a,b)
    jac[0,1] = dfix2(a,b)
    jac[1,0] = dfiix1(a,b)
    jac[1,1] = dfiix2(a,b)
    return jac

def multivariable_solve(fi,fii,tolx=10**-5,tolf=10**-5,x1i0 = 5.0,x2i0 = 2.0):

    fi_e,fii_e = evaluar(fi,fii)#variables para poder evaluarlas expresiones simbolicas
    iter = 0

    while True:
        iter += 1
        A = jaco(x1i0,x2i0,fi,fii)
        b = np.zeros([2,1])
        b[0] = -fi_e(x1i0, x2i0)
        b[1] = -fii_e(x1i0, x2i0)
        delta_x = np.linalg.solve(A,b)
        x_1 = np.float(x1i0 + delta_x[0])
        x_2 = np.float(x2i0 + delta_x[1])

        if np.abs(x_1-x1i0) <= tolx and np.abs(x_2-x2i0) <= tolx:
            break
        if np.abs(fi_e(x_1,x_2)) <= tolf and np.abs(fii_e(x_1,x_2)) <= tolf:
            break
        x1i0 = x_1
        x2i0 = x_2
    print("con {} iteraciones y {} de tolerancia,\nraiz x1: {} raiz x2: {}\n".format(iter,tolx,x_1,x_2))

x1 = sym.Symbol("x1")
x2 = sym.Symbol("x2")

f1 = 3.0*sym.exp(-(x1**2))-5.0*(x2)**(1.0/3.0)+6.0
f2 = 3.0*x1 + 0.5*(x2)**(1.0/4.0)-15.0
f3 = x1**2+x2-3
f4 = (x1-2)**2+(x2+3)**2-4

def lineas_contorno(fi,fii):
    delta = 0.1
    x_1 = np.arange(-2.0, 4.0, delta)
    x_2 = np.arange(-2.0, 4.0, delta)
    X1,X2 = np.meshgrid(x_1,x_2)
    fi_e, fii_e = evaluar(fi, fii)
    plt.figure()
    c1 = plt.contour(X1,X2,fi_e(X1,X2),colors="b")
    c2 = plt.contour(X1, X2, fii_e(X1, X2), colors="r")
    plt.clabel(c1)
    plt.clabel(c2)
    plt.grid(1)
    plt.show()

#multivariable_solve(f1,f2)
#lineas_contorno(f1,f2)

lineas_contorno(f3,f4)
multivariable_solve(f3,f4,x1i0=2,x2i0=-1)#el intervalo se definio con la grafica anterior
multivariable_solve(f3,f4,tolx=10**-10,tolf=10**-10)

