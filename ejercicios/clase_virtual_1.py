'''
es no lineal porque existe al menos una variable del vector x en el sistema Ax = b tiene exponente diferente de 1
'''
##
import numpy as np
import matplotlib.pyplot as plt

def f2(x):
    return -x**(0.25)+np.sin(3.5*x)+4*x**(0.5)+2*x - 5
x1 = np.arange(0,2,0.001)
plt.figure()
plt.plot(x1,f2(x1))
plt.grid(1)
plt.xlabel("x")
plt.ylabel("f2(x)")
plt.show()
minind1 = np.argmin(np.abs(f2(x1)))
print("con un cero de 0.001, la solución es {}".format(x1[minind1]))

##
import numpy as np
import matplotlib.pyplot as plt
def f2(x):
    return -x**(0.25)+np.sin(3.5*x)+4*x**(0.5)+2*x - 5

x2 = np.arange(0,2,0.00001)#tambien para 0001
plt.figure()
plt.plot(x2,f2(x2))
plt.grid(1)
plt.xlabel("x")
plt.ylabel("f2(x)")
plt.show()

minind2 = np.argmin(np.abs(f2(x2)))
print("con un cero de 0.00001, la solución es {}".format(x2[minind2]))
##
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return - (np.sqrt(3*x)**(2/5))+x**3*np.cos(3*x)+4*x**2 - 7
def f2(x):
    return -x**(0.25)+np.sin(3.5*x)+4*x**(0.5)+2*x - 5
x0 = 1.0
x1 = 2.0
tolx = 10**-10
tolf = tolx
x2prev = x1
iteraciones = 0
while True:
    iteraciones += 1
    x2 = (x0+x1)/2.0
    if np.abs(x2-x2prev) <= tolx:
        break
    if np.abs(f1(x2)) <= tolf:
        break
    if f1(x2)*f1(x0) < 0:
        x1=x2
    else:
        x0 = x2
    x2prev = x2
print("Biseccion: con {} iteraciones, la raiz es {} para tolerancias de 10**'10".format(iteraciones,x2))
##
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return - (np.sqrt(3*x)**(2/5))+x**3*np.cos(3*x)+4*x**2 - 7
def f2(x):
    return -x**(0.25)+np.sin(3.5*x)+4*x**(0.5)+2*x - 5
x0 = 1.0
x1 = 2.0
tolx = 10**-5
tolf = tolx
x2prev = x1
iteraciones = 0
while True:
    iteraciones += 1
    x2 = (x0+x1)/2.0
    if np.abs(x2-x2prev) <= tolx:
        break
    if np.abs(f1(x2)) <= tolf:
        break
    if f1(x2)*f1(x0) < 0:
        x1=x2
    else:
        x0 = x2
    x2prev = x2
print("Biseccion: con {} iteraciones, la raiz es {} para tolerancias de 10**-5".format(iteraciones,x2))
##falsa pos
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return - (np.sqrt(3*x)**(2/5))+x**3*np.cos(3*x)+4*x**2 - 7
def f2(x):
    return -x**(0.25)+np.sin(3.5*x)+4*x**(0.5)+2*x - 5
x0 = 1.0
x1 = 2.0
tolx = 10**-10
tolf = tolx
x2prev = x1
iteraciones = 0
while True:
    iteraciones+=1
    x2 = x1 - (f1(x1)*(x1-x0)/(f1(x1)-f1(x0)))
    if np.abs(x2-x2prev) <= tolx:
        break
    if np.abs(f1(x2)) <= tolf:
        break
    if f1(x2)*f1(x0) < 0:
        x1=x2
    else:
        x0 = x2
    x2prev = x2
print("con {} iteraciones, {} de tolerancia, la raiz es: {}".format(iteraciones,tolx,x2))
##callback
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
    print("Biseccion: con {} iteraciones, la raiz es {} para tolerancias de 10**-5".format(iteraciones,x2))

falsapos(f1,10**-10)
#biseccion(f1,10**-10)
falsapos(f2,10**-5)
falsapos(f2,10**-10)
#biseccion(f2,10**-10)

