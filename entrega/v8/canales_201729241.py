import numpy as np
import matplotlib.pyplot as plt


def F1(y2):
    return y2
def F2(t,y1,y2):
    return 2.0 *y2-4.0*y1+8.0*t-12.0*np.sin(2.0*t)
def F2EulerBack(t,y1,y2,h):
    return(y2+h*(-4.0*y1*8.0*t-12.0*np.sin(2.0*t)))/(1-2*h+4*(h**2))
def F2EulerMod(t1,t2,y1,y2,h):
    return (y2+(h/2.0)*(F2(t1,y1,y2)-4.0*(y1+(h/2.0)*y2)
                            +8.0 *t2 - 12.0 *np.sin(2.0*t2)))/(1-h+(h**2))
def FEulerModRoot(yt2,t1,t2,y1t1,y2t1,h):
    return[y1t1 + (h/2.0)*\
           (F1(y2t1)+F1(yt2[1]))-yt2[0],
           y2t1 + (h/2.0)*\
           (F2(t1,y1t1,y2t1)+F2(t2,yt2[0],yt2[1]))-yt2[1]]
def todas(h=0.01):

    Y10 = -2
    Y20 = 8
    T0 = 0.0
    Tf = 10.0
    T = np.arange(T0, Tf + h, h)

    Y1EulerFor = np.zeros(np.size(T))
    Y1EulerBack = np.zeros(np.size(T))
    Y1EulerMod = np.zeros(np.size(T))
    Y1EulerModRoot = np.zeros(np.size(T))
    Y1RK2 = np.zeros(len(T))
    Y1RK4 = np.zeros(len(T))

    Y1EulerFor[0] = Y10
    Y1EulerBack[0] = Y10
    Y1EulerMod[0] = Y10
    Y1EulerModRoot[0] =Y10
    Y1RK2[0] = Y10
    Y1RK4[0] = Y10

    Y2EulerFor = np.zeros(np.size(T))
    Y2EulerBack = np.zeros(np.size(T))
    Y2EulerMod = np.zeros(np.size(T))
    Y2EulerModRoot = np.zeros(np.size(T))
    Y2RK2 = np.zeros(len(T))
    Y2RK4 = np.zeros(len(T))

    Y2EulerFor[0] = Y20
    Y2EulerBack[0] = Y20
    Y2EulerMod[0] = Y20
    Y2EulerModRoot[0] = Y20
    Y2RK2[0] = Y20
    Y2RK4[0] = Y20






    for i in range(1, np.size(T)):
        Y1EulerFor[i] = Y1EulerFor[i-1] + h*F1(T[i-1],Y1EulerFor[i-1])
        #Y2EulerFor[i] = Y2EulerFor[i - 1] + h * F2(T[i - 1], Y2EulerFor[i - 1])

        #Y2EulerBack[i] = F2EulerBack(T[i], Y1EulerBack[i - 1], Y2EulerBack[i - 1], h)
        Y1EulerBack[i] = Y1EulerBack[i-1] + h* F1(Y2EulerBack[i])

        #Y2EulerMod[i]=F2EulerMod(T[i-1],T[iter],Y1EulerMod[i-1], Y2EulerMod[i-2],h)
        Y1EulerMod[i] = Y1EulerMod[i - 1] + (h / 2.0) * F1(Y2EulerMod[i - 1]+F1(Y2EulerMod[i]))

        #SolMod = opt.fsolve(FeulerModRoot,np.array([Y1EulerModRoot[i]]))
        k1 = F1(T[i-1],Y1RK2[i-1])
        k2 = F1(T[i-1]+h,Y1RK2[i-1]+k1*h)
        Y1RK2[i] = Y1RK2[i-1]+(h/2.0)*(k1+k2)

        k11 = F1(Y2RK2[i - 1])
        k21 = F2(T[i-1],Y1RK2[i-1],Y2RK2[i-1])
        k12 = F1(Y2RK2[i-1]+k21*h)
        k22 = F2(T[i-1]+0.5*h,Y1RK2[i-1]+k11*h,
                 Y2RK2[i-1]+k21*h)
        Y1RK2[i]=Y1RK2[i-1]+(h/2.0)*(k11+k12)
        #Y2RK2[i] = Y2RK2[i - 1] + (h / 2.0) * (k21 + k22)

        #r4

        k11 = F1(Y2RK4[i - 1])
        k21 = F2(T[i-1],Y1RK4[i-1],Y2RK4[i-1])
        k12 = F1(Y2RK4[i-1]+k21*h)
        k22 = F2(T[i-1]+0.5*h,Y1RK4[i-1]+0.5*k11*h,
                 Y2RK4[i-1]+0.5*k21*h)
        k13 = F1(Y2RK4[i-1]+0.5*k22*h)
        k23 = F2(T[i-1] +0.5*h,Y1RK4[i-1]+0.5*k12*h,Y2RK4[i-1]+0.5*k22*h)
        k14 = F1(Y2RK4[i-1]+k23*h)
        k24 = F2(T[i-1] + h,Y1RK4[i-1]+k13*h,Y2RK4[i-1]+0.5*k23*h)

        Y1RK4[i] = Y1RK4[i-1]+(h/6.0)*(k11+2.0*k12+2.0*k13+k14)
        #Y2RK4[i] = Y2RK4[i-1]+(h/6.0)*(k21+2.0*k22+2.0*k23+k24)



    plt.figure()
    plt.title("estimaciones y1")
    plt.plot(T, Y1EulerFor, "r", label="forward")
    plt.plot(T, Y1EulerBack, "g", label="back")
    plt.plot(T, Y1EulerMod, "m", label="mod")
    plt.plot(T,Y1RK2,"orange",label="RK2")
    plt.plot(T, Y1RK4, "maroon", label="RK4")
    
    # plt.text()
    plt.xlabel("t", fontsize=15)
    plt.ylabel("Y(t)", fontsize=15)
    plt.legend()
    plt.grid(True)
    plt.show()
    
    plt.figure()
    plt.title("estimaciones y2")
    plt.plot(T, Y2EulerFor, "r", label="forward")
    plt.plot(T, Y2EulerBack, "g", label="back")
    plt.plot(T, Y2EulerMod, "m", label="mod")
    plt.plot(T,Y2RK2,"orange",label="RK2")
    plt.plot(T, Y2RK4, "maroon", label="RK4")

    # plt.text()
    plt.xlabel("t", fontsize=15)
    plt.ylabel("Y(t)", fontsize=15)
    plt.legend()
    plt.grid(True)
    plt.show()

def analitic(t):
    a=2
    b=0
    So=0.99
    Io = 1- So
    N = So + Io
    return ((a*N-b)*Io*np.exp((a*N-b)*t))/((a*N-b)+a*Io*(np.exp((a*N-b)*t)-1))

todas()