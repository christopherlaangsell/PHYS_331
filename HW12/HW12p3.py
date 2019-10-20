import numpy as np
import matplotlib.pyplot as plt

#dir(np)

def RK4integrate(F,x,y,xStop,h):
    def run_kut4(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x+h/2.0, y+K0/2.0)
        K2 = h*F(x+h/2.0, y+K1/2.0)
        K3 = h*F(x+h, y+K2)
        return (K0 +2.0*K1+2.0*K2+K3)/6.0
    
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop-x)
        y = y + run_kut4(F,x,y,h)
        x = x+h
        X.append(x)
        Y.append(y)
        
    return np.array(X), np.array(Y)


def Fcoupled(x,y):
    #y = theta. x = t
    return np.array([y[1],-np.sin(y[0])])

theta = np.array([1,0])

x,y = RK4integrate(Fcoupled,0,theta,15,.001)

plt.plot(x,y)
plt.grid(True)
plt.legend(["Theta","Derivative"])
plt.title("Pendulum")
plt.show()

g = 9.8

tau = x[np.argmax(y[1:,0])+1]-x[np.argmax(y[:,0])]
period = tau/(np.sqrt(g))

print()
print("period = " + str(period) + " seconds")
