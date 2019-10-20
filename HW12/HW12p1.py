import numpy as np
import matplotlib.pyplot as plt
import scipy as spy

def EulerIntegrate(f, xstart, xstop, y0, h):
    ylist = [y0]
    xmesh = np.arange(xstart,xstop,h)
    
    
    for i in range(len(xmesh)-1):
        ynext = ylist[i]+f(xmesh[i],ylist[i])*h
        ylist.append(ynext)
    
    return (xmesh,ylist)
    
def f1(x,y):
    return x-2*x*y


def plot():
    h = np.array([.3,.1,.01])
    
    for i in range(3):
        x,y = EulerIntegrate(f1,-1,4,4,h[i])
        
        plt.plot(x,y,'.', label = "h = "+str(h[i]))
    
    xrange = np.arange(-1,4,.01)
    plt.plot(xrange, (3.5*np.e)*np.e**(-1*xrange**2)+.5,label = "analytical solution")
    plt.legend()
    plt.title("EulerIntegration")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()
    
    
    
    for i in range(3):
        x,y = EulerIntegrate(f1,-1,4,4,h[i])
        
        plt.plot(x,y,'.', label = "h = "+str(h[i]))
    
    xrange = np.arange(-1,4,.01)
    plt.plot(xrange, (3.5*np.e)*np.e**(-1*xrange**2)+.5,label = "analytical solution")
    plt.legend()
    plt.title("EulerIntegrationZoomed")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(-.5,.5)
    plt.grid(True)
    plt.show()
    
    
    for i in range(3):
        x,y = EulerIntegrate(f1,-1,4,4,h[i])
        
        plt.plot(x,y,'.', label = "h = "+str(h[i]))
    
    xrange = np.arange(-1,4,.01)
    plt.plot(xrange, (3.5*np.e)*np.e**(-1*xrange**2)+.5,label = "analytical solution")
    plt.legend()
    plt.title("EulerIntegrationZoomed")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(1,2)
    plt.grid(True)
    plt.show()
    
    
plot()



