import numpy as np


def lagrange(x,y,xk):
    yk = np.zeros(np.size(xk))
    for k in range(np.size(xk)):
        for i in range(np.size(y)):
            multaux = 1
            for j in range(np.size(y)):
                if i == j:
                    continue
                multaux *= (xk[k] - x[j]) / (x[i] - x[j])
            yk[k] += y[i]*multaux
    return yk
def valores_python(x,y,xk):
    cipoly = np.polyfit(x,y,np.size(x)-1)
    ykpoly = np.polyval(cipoly,xk)
    return ykpoly
#puntos conocidos
xi = np.array([13,16,17,23,28,33])
yi = np.array([30,92,21,159,96,236])
#los valores que quiero conocer
xk = np.array([14,18,20,22,24,26,30,31])
#xk = np.array([15,19,21,25,27,29])



print(lagrange(xi,yi,xk))
print(valores_python(xi,yi,xk))
