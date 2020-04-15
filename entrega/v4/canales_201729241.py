

## secante tasa de convergencia
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
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
    iter_array = np.arange(1.0,np.size(tasas_convergencias)+1)
    plt.figure()
    plt.plot(iter_array,tasas_convergencias)
    plt.plot(iter_array,tasas_convergencias,"or")
    plt.show()

print("f1")
secante(funcion1,10**-10)
secante(funcion1,10**-15)
print("f2")
secante(funcion2,10**-5)
secante(funcion2,10**-15)