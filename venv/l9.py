import numpy as np
import struct as st
import matplotlib.pyplot as plt
import scipy.interpolate as inter

# punto1
def polinomial(xi, yi, xk):
    Ci = coef_val(xi, yi)
    # Ci = np.polyfit(xi,yi,np.size(xi)-1)

    N = np.size(Ci)
    yk = np.zeros(np.size(xk))
    for i in range(np.size(xk)):
        for j in range(N):
            yk[i] \
                += Ci[j] \
                   * (xk[i] ** (N - j - 1))
    return yk


def coef_val(xi, yi):
    N = np.size(xi)
    A = np.zeros([N, N])
    b = np.zeros([N, 1])
    for i in range(N):
        for j in range(N):
            A[i, j] = xi[i] ** (N - j - 1)
        b[i] = yi[i]
    Ci = np.linalg.solve(A, b)
    return Ci

#punto 2
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

def punto3(xi,yi,xk):
    f = open("punto3.txt","w")
    poli = polinomial(xi,yi,xk)
    lag = lagrange(xi,yi,xk)
    nump = valores_python(xi,yi,xk)

    f.write("X_new \t{:^30s}\t{:^25s}\t\t{:^25s}\n".format("y_new(polinomial)","y_new(lagrange)","y_new(numpy)"))
    for i in range(np.size(xk)):
        f.write("{:}\t{: 25.10}\t{: 25.10}\t{: 25.10}\n".format(xk[i],poli[i],lag[i],nump[i]))
    f.close()
def punto4(xi,yi,xk):
    f = open("punto4.txt", "w")
    f.write("X_new \t{:^30s}\t{:^25s}\t\t{:^25s}\n".format("y_new(polinomial)", "y_new(lagrange)", "y_new(numpy)"))
    for i in range(0, np.size(xk) - 1, 4):  # Salte cada 8 espacios
        # Modifica xi y yi para obtener sólo 4 puntos con saltos de 4
        v = xi[i:i + 4]
        u = yi[i:i + 4]
        poli = polinomial(v,u,xk[i:i + 4] )
        lag = lagrange(v,u,xk[i:i + 4])
        nump = valores_python(v,u,xk[i:i + 4])

        for j in range(np.size(poli)):
            f.write("{:}\t{: 25.10}\t{: 25.10}\t{: 25.10}\n".format(xk[i+j],poli[j],lag[j], nump[j]))
    f.close()

def punto5(xi,yi,xk):
    nat = inter.CubicSpline(xi,yi,bc_type="natural")
    f=open("punto5.txt","w")
    f.write("X_new \t{:^25s}\n".format("y_new(polinomial)"))
    for i in xk:
        f.write("{:}\t\t{:}\n".format(i,nat(i)))
    f.close()
def punto6():
    pass
f = open("x_obs.bin","rb")
file = f.read()
xi = np.array(list(st.unpack("d"*int(len(file)/8),file)))
f.close()
f = open("y_obs.bin", "rb")
file = f.read()
yi = np.array(list(st.unpack("d" *int(len(file) / 8), file)))
f.close()
xk = [78.12, 0.98, 67.59, 8.69, 55.69, 48.12, 13.24, 97.56, 25.69, 1.26]

punto3(xi,yi,xk)
punto4(xi,yi,xk)
punto5(xi,yi,xk)
