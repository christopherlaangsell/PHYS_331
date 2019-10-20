# Template File for Homework 3, Problem 3
# PHYS 331
# Amy Oldenburg

import numpy as np
import matplotlib.pyplot as plt

## module newtonRaphson
''' root = newtonRaphson(f,df,a,b,tol).
    Finds a root of f(x) = 0 by combining the Newton-Raphson
    method with bisection. The root must be bracketed in (a,b).
    Calls user-supplied functions f(x) and its derivative df(x).   
'''    
def newtonRaphson(f,df,a,b,tol): # DO NOT MODIFY
    from numpy import sign
    
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): 
        print('Root is not bracketed')
        return []
    x = 0.5*(a + b)                    
    for i in range(30):
        fx = f(x)
        if fx == 0.0: return x
      # Tighten the brackets on the root 
        if sign(fa) != sign(fx): b = x  
        else: a = x
      # Try a Newton-Raphson step    
        dfx = df(x)
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx
      # If the result is outside the brackets, use bisection  
        if (b - x)*(x - a) < 0.0:  
            dx = 0.5*(b - a)                      
            x = a + dx
      # Check for convergence     
        if abs(dx) < tol*max(abs(b),1.0): return x
    print('Too many iterations in Newton-Raphson')
    
## ADD your code below this line


 
def func(x):
    return np.cosh(x)*np.cos(x)+1

def deriv(x):
    return np.cos(x)*np.sinh(x)-np.sin(x)*np.cosh(x)    #derivative
    
    
x=np.arange(0,10,.01)
plt.plot(x, func(x))
plt.ylim(-15, 15)
plt.grid(True)


root = newtonRaphson(func,deriv,0,10,10**-10)




v = (2.5*1000*25*1000*.9)    #defining all variables
md = (7850) 
m = v*md
l = .9
e = 2*10**8
i = (25*1000*(2.5*1000)**3)/12

f = (1/(2*3.14))*(np.sqrt((root**4)*e*i)/(m*(l**3)))   #rearranged eq from book

root1 = newtonRaphson(func, deriv, 1, 3, 10**-10)   #finding the two roots
root2 = newtonRaphson(func, deriv, 4,6,10**-10)

plt.show()

print('root on a given positive interval' + ' = ' + str(root1))
print('root on a given positive interval' + ' = ' + str(root2))
