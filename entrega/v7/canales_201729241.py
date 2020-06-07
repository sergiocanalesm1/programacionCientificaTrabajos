import numpy as np
import matplotlib.pyplot as plt

def F1(t,y):
    return (0.49 -((0.00245*np.exp(0.49*t))/ (0.49 + 0.005 *(np.exp(0.49*t)-1))))*y
def Feuback(t,y,h):
    return y/(1-h*(0.49 -((0.00245*np.exp(0.49*t))/ (0.49 + 0.005 *(np.exp(0.49*t)-1)))))
def F1euMod(t,h):
    return (1-(h/2.0)*
            (0.49-((0.00245 * np.exp(0.49*t))/
                   (0.49+0.005*(np.exp(0.49*t)-1)))))

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
        #YeulerForward[i] = YeulerForward[i-1] + h*F1(T[i-1],YeulerForward[i-1])
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

def eulerMod(h=0.01):
    Y0 = 0.01
    T0 = 0.0
    Tf = 30.0
    T = np.arange(T0, Tf + h, h)
    Y = np.zeros(len(T))
    Y[0]= Y0
    for i in range(1, len(T)):
        Y[i] = (Y[i-1]+(h/2.0)*F1(T[i-1],T[i-1]))/F1euMod(T[i],h)
    graficar(T,Y,analitic(T),h)
def todas(h=0.01):

    Y0 = 0.01
    T0 = 0.0
    Tf = 30.0
    T = np.arange(T0, Tf + h, h)
    YeulerForward = np.zeros(np.size(T))
    YeulerBack = np.zeros(np.size(T))
    Yeumod = np.zeros(np.size(T))
    YRK2 = np.zeros(len(T))
    YRK4 = np.zeros(len(T))
    YeulerForward[0] = Y0
    YeulerBack[0] = Y0
    Yeumod[0] = Y0
    YRK2[0] = Y0
    YRK4[0] = Y0
    for i in range(1, np.size(T)):
        YeulerForward[i] = YeulerForward[i-1] + h*F1(T[i-1],YeulerForward[i-1])
        YeulerBack[i] = Feuback(T[i - 1], YeulerBack[i - 1], h)
        Yeumod[i] = (Yeumod[i - 1] +
                     (h / 2.0) * F1(T[i - 1], Yeumod[i - 1])) / F1euMod(T[i], h)
        k1 = F1(T[i-1],YRK2[i-1])
        k2 = F1(T[i-1]+h,YRK2[i-1]+k1*h)
        YRK2[i] = YRK2[i-1]+(h/2.0)*(k1+k2)

        k1 = F1(T[i - 1], YRK4[i - 1])
        k2 = F1(T[i-1]+0.5*h,YRK4[i-1]+0.5*k1*h)
        k3 = F1(T[i - 1] + 0.5 * h, YRK4[i - 1] + 0.5 * k2 * h)
        k4 = F1(T[i -1]+h,YRK4[i-1]+k3*h)
        YRK4[i] = YRK4[i-1] +(h/6.0) * (k1+2.0*k2+2.0*k3+k4)

    plt.figure()
    plt.title("h = " + str(h))
    plt.plot(T, YeulerForward, "r", label="forward")
    plt.plot(T, YeulerBack, "g", label="back")
    plt.plot(T, Yeumod, "k", label="mod")
    plt.plot(T,YRK2,"y",label="RK2")
    plt.plot(T, YRK4, "m", label="RK4")
    plt.plot(T, analitic(T), "--b", label="analitic")
    # plt.text()
    plt.xlabel("t", fontsize=15)
    plt.ylabel("Y(t)", fontsize=15)
    plt.legend()
    plt.grid(True)
    plt.show()
def RK2(h=0.01):
    Y0 = 0.01
    T0 = 0.0
    Tf = 30.0
    T = np.arange(T0, Tf + h, h)
    YRK2 = np.zeros(len(T))
    YRK2[0] = Y0
    for i in range(1,len(T)):
        k1 = F1(T[i - 1], YRK2[i - 1])
        k2 = F1(T[i - 1] + h, YRK2[i - 1] + k1 * h)
        YRK2[i] = YRK2[i - 1] + (h / 2.0) * (k1 + k2)
    graficar(T,YRK2,analitic(T),h)
def analitic(t):
    a=0.5
    b=0.01
    So=0.99
    Io = 1- So
    N = So + Io
    return ((a*N-b)*Io*np.exp((a*N-b)*t))/((a*N-b)+a*Io*(np.exp((a*N-b)*t)-1))

def graficar(T,eu,anal,h):
    plt.figure()
    plt.title("h = "+str(h))
    plt.plot(T, eu, "r",label="euler")
    plt.plot(T, anal,"b",label="analitic")
    #plt.text()
    plt.xlabel("t", fontsize=15)
    plt.ylabel("Y(t)", fontsize=15)
    plt.legend()
    plt.grid(True)
    plt.show()


h=[5.0,1.0,0.5,0.1,0.05]
for x in h:
    todas(x)


