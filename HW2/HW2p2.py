# Template File for Homework 2, Problem 2
# PHYS 331
# Amy Oldenburg
import numpy as np
import matplotlib.pyplot as plt

def rf_bisect(f,xlo,xhi,xtol,nmax):
#Computes the value of the root for function f bracketed in the domain [xlo, xhi]. 
# PARAMETERS:
#   f     --  (function) The one-dimensional function to evaluate a root of.
#   xlo   --  (float) The lower limit of the bracket.
#   xhi   --  (float) The upper limit of the bracket.
#   xtol  --  (float) The tolerance the calculated root should achieve.
#   nmax  --  (int) The maximum number of iterations allowed.

# RETURNS: (tuple(float, int)) A root of f that meets the tolerance tol the number 
# of iteratons required to converge.
    
#----> Implement your solution for rf_bisect here <-------
   
    xlow = xlo     #setting new variables for parameters
    xhigh = xhi
    iters = 1
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

# Functions f1, f2, f3, and f4 that may be used to test your implementation of rf_bisect.
def f1(x):
    return 3 * x + np.sin(x) - np.exp(x)

def f2(x):
    return x**3

def f3(x):
    return np.sin(1. / (x + 0.01))

def f4(x):
    return 1. / (x - 0.5)


# Example: Find the root of f2(x) and print the result.

#(root,iters) = rf_bisect(f1, -1., 1., 1e-6, 25)
#print('Root of f1: ' + str(root))
#print('# iterations: ' + str(iters))
#fval=f1(root)
#print('f1 evaluated at root is: ' + str(fval))

#----> (Hint: you might consider shortcuts to automate)
# (it's OK if you write additional functions to perform repetitive tasks)



def root(func, tolerance):
    for f in func:
        for t in tolerance :
            (root, total_iteration) = rf_bisect(f,-1.,1.,t,25)
            print('Root of ' + f.__name__ + " " + str(root)) #setting up print screen to be clear
            print('Tolerance: ' + str(t))
            print('# iterations: ' + str(total_iteration))
            fval = f2(root)
            print(f.__name__ + ' evaluated at root is: ' + str(fval))
            
f = [f1,f2,f3]
t = [10**-3, 10**-6, 10**-12]


#A plot for all the graphs
x = np.arange(-1,1,.001)
plt.plot(x, f1(x), label = 'f1')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1,1)
plt.grid(True)
plt.show()

x = np.arange(-1,1,.001)
plt.plot(x, f2(x), label = 'f2')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1,1)
plt.grid(True)
plt.show()

x = np.arange(-1,1,.001)
plt.plot(x, f3(x), label = 'f3')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1,1)
plt.grid(True)
plt.show()

x = np.arange(-1,1,.001)
plt.plot(x, f4(x), label = 'f4')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1,1)
plt.grid(True)
plt.show()

root(f, t)
            