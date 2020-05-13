import numpy as np
import matplotlib.pyplot as plt

def F1(t,y):
    return (0.49 -((0.00245*np.exp(0.49*t))/ (0.49 + 0.005 *(np.exp(0.49*t)-1))))*y
def Feuback(t,y,h):
    return y/(1-h*(0.49 -((0.00245*np.exp(0.49*t))/ (0.49 + 0.005 *(np.exp(0.49*t)-1)))))
def eulerBack(h=0.01):

    Y0 = 0.01
    T0 = 0.0
    Tf = 30.0
    T = np.arange(T0, Tf + h, h)
    YeulerForward = np.zeros(np.size(T))
    YeulerBack = np.zeros(np.size(T))
    YeulerForward[0] = Y0
    YeulerBack[0] = Y0
    for i in range(1,np.size(T)):
        YeulerForward[i] = YeulerForward[i-1] + h*F1(T[i-1],YeulerForward[i-1])
        YeulerBack[i] = Feuback(T[i-1],YeulerBack[i-1],h)
    graficar(T,YeulerForward,YeulerBack,analitic(T),h)

def eulerForward(h=0.01):
    Y0 = 0.01
    T0 = 0.0
    Tf = 30.0
    T = np.arange(T0, Tf + h, h)
    YeulerForward = np.zeros(np.size(T))
    YeulerForward[0] = Y0

    for i in range(1, np.size(T)):
        YeulerForward[i] = YeulerForward[i - 1] + h * F1(T[i - 1], YeulerForward[i - 1])
    graficar(T, YeulerForward, analitic(T), h)


def analitic(t):
    a=0.5
    b=0.01
    So=0.99
    Io = 1- So
    N = So + Io
    return ((a*N-b)*Io*np.exp((a*N-b)*t))/((a*N-b)+a*Io*(np.exp((a*N-b)*t)-1))

def graficar(T,eu,anal,h):
    plt.figure()
    plt.title("h = "+h)
    plt.plot(T, eu, "r",label="forward")
    plt.plot(T, anal,"b",label="analitic")
    plt.text()
    plt.xlabel("t", fontsize=15)
    plt.ylabel("Y(t)", fontsize=15)
    plt.legend()
    plt.grid(True)
    plt.show()


h=[5.0,1.0,0.5,0.1,0.05]

for i in h:
    eulerBack(h=i)

