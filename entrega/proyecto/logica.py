import scipy as sc
import numpy as np
import math
from scipy.signal import find_peaks
from scipy.misc import electrocardiogram
import matplotlib.pyplot as plt

def hallarHR(ecg = electrocardiogram(),fs=360,h=0.5,w=5):
    time = np.arange(ecg.size)/fs
    peaks, properties = find_peaks(ecg,height=h,width=w)#x y y de HR
    tacograma = np.diff(time[peaks])#la diferencia entre cada pico
    bpm = 60/tacograma #latidos por minuto
    HR = np.mean(bpm)

    """
    plt.figure()
    plt.plot(time,ecg)
    plt.plot(peaks/fs,ecg[peaks],"o")
    plt.show()
    """
    return HR

def ecg(v,t,w,ai,bi,thi):#ignorar esta, era para porobar con scipy pero no se como hacerlo
    a = 1 - np.sqrt(v[1]**2+v[0]**2)
    w = 2*np.pi*(59.7+np.random.randint(0,6)/10)#generar un valor aleatorio del 5% en el 60
    dx = v[0]*a - v[1]*w
    dy = v[1]*a + v[0]*w
    dthi = (math.atan2(v[1]/v[0]) - thi) % 2*np.pi
    f2 = 0.25 #4 respiraciones por segundo
    z=0.5 #creo que debe estar entre -0.5 y 1.5
    A = 0.15
    z0 = A*np.sin(2*np.pi*f2*t)
    dz = - np.sum(ai*dthi*np.exp(dthi**2/(2*bi**2)))-(z-z0)

def F1(x,y,Trr):
    a = 1 - np.sqrt(x**2+y**2)
    w = (2*np.pi/Trr)
    return a*x - w*y

def F2(x,y,Trr):
    a = 1 - np.sqrt(x**2 + y**2)
    w = (2 * np.pi / Trr)
    return a*y + w*x
def F3(x,y,a,b,theta,t,z):
    Fsum = 0
    A = 0.15
    f2 = 0.25  # 4 respiraciones por segundo
    THETA = np.arctan2(y,x)
    z0 = A*np.sin(2*np.pi*f2*t)

    for i in range(len(a)):# P,Q,R,S,T
        dthi = np.fmod(THETA - theta[i], 2*np.pi) #para negativos y positivos usar fmod
        Fsum += a[i]*dthi*np.exp(-(dthi**2)/(2*b[i]**2))

    return -Fsum - (z - z0)

#ecuacion y/(1-h*F)
def F1euback(x, y,Trr,h):
    a = 1 - np.sqrt(x**2 + y**2)
    w = 2*np.pi/Trr
    return y / (1 - h * (a*x - w*y))

def F2euback(x, y,Trr,h):
    a = 1 - np.sqrt(x**2 + y**2)
    w = 2*np.pi/Trr
    return y / (1 - h * (a*y + w*y))


def F1euMod(t, h):
    return (1 - (h / 2.0) *
            (0.49 - ((0.00245 * np.exp(0.49 * t)) /
                     (0.49 + 0.005 * (np.exp(0.49 * t) - 1)))))
#,t=[-0.2,-0.05,0,0.05,0.3]
def calcular(a = [1.2,-5.0,30.0,-7.5,0.75],b = [0.25,0.1,0.1,0.1,0.4],theta = [(-1/3)*np.pi,(-1/12)*np.pi,0,(1/12)*np.pi,(1/2)*np.pi], FC=80, Tf=30.0, fs=360):#fc es frecuencia cardiaca, tf es numero de latidos, fs es frecuencia muestreo
    Y0 = 0.0
    X0 = 1.0#como es un circulo unitario, X0+Y0 tiene que ser igual a 1
    Z0 = 0.3#valor entre 0 y 0.5
    T0 = 0.0
    h = 1 / fs
    T = np.arange(T0, Tf + h, h)

    #para calcular el tiempo entre R y más adelante calcular el w
    meanFC = 60 / FC
    stdFC = meanFC * 0.05#la desviacion debería ser del 5%
    tRR = np.random.normal(meanFC, stdFC, np.size(T))#arreglo con len(T) numeros aleatorios

    XeulerForward = np.zeros(np.size(T))
    XeulerForward[0] = X0
    YeulerForward = np.zeros(np.size(T))
    YeulerForward[0] = Y0
    ZeulerForward = np.zeros(np.size(T))
    ZeulerForward[0] = Z0

    YeulerBack = np.zeros(np.size(T))
    Yeumod = np.zeros(np.size(T))
    YRK2 = np.zeros(len(T))
    YRK4 = np.zeros(len(T))

    YeulerBack[0] = Y0
    Yeumod[0] = Y0
    YRK2[0] = Y0
    YRK4[0] = Y0
    for i in range(1, np.size(T)):

        XeulerForward[i] = XeulerForward[i - 1] + h*F1(XeulerForward[i - 1],YeulerForward[i - 1],1/tRR[i])
        YeulerForward[i] = YeulerForward[i - 1] + h*F2(XeulerForward[i - 1],YeulerForward[i - 1], 1/tRR[i])
        ZeulerForward[i] = ZeulerForward[i - 1] + h*F3(XeulerForward[i - 1],YeulerForward[i - 1],a,b,theta,T[i],ZeulerForward[i-1])
        """
        YeulerBack[i] = Feuback(T[i - 1], YeulerBack[i - 1], h)
        Yeumod[i] = (Yeumod[i - 1] +
                     (h / 2.0) * F1(T[i - 1], Yeumod[i - 1])) / F1euMod(T[i], h)
        k1 = F1(T[i - 1], YRK2[i - 1])
        k2 = F1(T[i - 1] + h, YRK2[i - 1] + k1 * h)
        YRK2[i] = YRK2[i - 1] + (h / 2.0) * (k1 + k2)

        k1 = F1(T[i - 1], YRK4[i - 1])
        k2 = F1(T[i - 1] + 0.5 * h, YRK4[i - 1] + 0.5 * k1 * h)
        k3 = F1(T[i - 1] + 0.5 * h, YRK4[i - 1] + 0.5 * k2 * h)
        k4 = F1(T[i - 1] + h, YRK4[i - 1] + k3 * h)
        YRK4[i] = YRK4[i - 1] + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        """
    plt.figure()
    plt.plot(T,ZeulerForward)
    plt.show()

np.seterr('raise')#para poder ver el error de runtime error
calcular()