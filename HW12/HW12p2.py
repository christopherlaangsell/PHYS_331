import numpy as np
import matplotlib.pyplot as plt

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
    return np.array([y[1],x-(2*x+3)*y[1]-6*x*y[0]])


def main():
    y0 = np.array([1.,1])
    
    h = np.array([1,.1,.01,.001])
    for i in range(len(h)):
        x,y = RK4integrate(Fcoupled,0,y0,4,h[i])
        plt.plot(x,y)
        
    plt.grid(True)
    plt.title("Runge Kutta Integration Consolodated")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.legend(["h = 1", "h = .1", "h = .01", "h = .001"])
    plt.show()
    
    x,y = RK4integrate(Fcoupled,0,y0,4,.001)
    plt.plot(x,y)
    plt.grid(True)
    plt.title("RK when h = .001")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.legend(["y1(x)","y2(x)  (Derivative)"])
    plt.show()
    
    x,y = RK4integrate(Fcoupled,0,y0,4,.01)
    plt.plot(x,y)
    plt.grid(True)
    plt.title("RK when h = .01")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.legend(["y1(x)","y2(x)  (Derivative)"])
    plt.show()
    
    x,y = RK4integrate(Fcoupled,0,y0,4,.1)
    plt.plot(x,y)
    plt.grid(True)
    plt.title("RK when h = .1")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.legend(["y1(x)","y2(x)  (Derivative)"])
    plt.show()
    
    x,y = RK4integrate(Fcoupled,0,y0,4,1)
    plt.plot(x,y)
    plt.grid(True)
    plt.title("RK when h = 1")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.legend(["y1(x)","y2(x)  (Derivative)"])
    plt.show()
    
main()