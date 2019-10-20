import numpy as np
import matplotlib.pyplot as plt

def rf_bisect(f,xlo,xhi,xtol,nmax):
  
    xlow = xlo     #setting new variables for parameters
    xhigh = xhi
    iters = 1
    midpoint = (xlo+xhi)/2.0    #first midpoint and potential root
    root = midpoint
    xmids = np.array([midpoint])
    fmids = np.array([f(midpoint)])
    
    
    
    
    for i in range(0,nmax):    #up to max iterations
        
         #if you are within tolerance break because you're done
        if np.abs(xlow-xhigh)<xtol:
            break
       
        # handle if your break lands on direct root
        if f(midpoint) == 0.0:
            break
       
        #if sign change occurs on left side, move midpoint left
        if f(xlow)/f(midpoint) < 0:
            xhigh = midpoint 
        #if sign change occurs on right side, move  midpoint right
        elif f(xhigh)/f(midpoint) < 0:
            xlow = midpoint
            
            
            
        #make new midpoint, add counter for iterations, and assign root as midpoint
        midpoint = (xlow+xhigh)/2.0
        iters += 1 
        root = midpoint
        xmids = np.append(xmids,[midpoint])
        fmids = np.append(fmids,[f(midpoint)])
    
        #print(xmids)
        

    return (xmids, fmids)
  
  
  
# Functions f1, f2, f3, and f4 that may be used to test your implementation of rf_bisect.
def f1(x):
    return 3 * x + np.sin(x) - np.exp(x)

def f2(x):
    return x**3

def f3(x):
    return np.sin(1. / (x + 0.01))

def f4(x):
    return 1. / (x - 0.5)
    
    

      


def root(func, tolerance):
    for f in func:
        for t in tolerance:
            (x,fx)= rf_bisect(f,0,1.,t,25)
            arrangement = np.arange(0,1,.001)
            plt.plot(arrangement, f(arrangement))
            error = []
            a = len(x)-1
            d = x[a]
            for i in range(0,len(x)): 
                error.append(d)
            error2 = np.asarray(error) #determining error rates
            print(error2)
            y = error2 - x
            print(y) 
            plt.plot(x,fx,'o')
            plt.grid(True)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()
            plt.plot(y,'o')
            plt.show
        

root([f1,f2,f3],[1e-12])