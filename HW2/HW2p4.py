import numpy as np
import matplotlib.pyplot as plt

def rf_bisect(f,xlo,xhi,xtol,nmax):

   
    xlow = xlo     #setting new variables for parameters
    xhigh = xhi
    iters = 0
    midpoint = (xlo+xhi)/2.0    #first midpoint and potential root
    root = midpoint

    
    
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
    
    

    return (root, iters)


def bern(h): #Bernouli's equation
    Q = 1.2
    g = 9.81
    b = 1.8
    h0 = .6
    H = .075
    
    return (Q**2/(2*g*(b**2)*(h**2)))+h+H-(Q**2/(2*g*(b**2)*(h0**2)))-h0


h = np.arange(.1,1,.001)
plt.plot(h, bern(h))
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
t = .90    #tolerance level pretty high because I still get 25 iterations
(root,total_iteration) = rf_bisect(bern, .1, 1., t, 25)
print('Root of ' + str(bern(h)))
print('# iterations: ' + str(total_iteration))