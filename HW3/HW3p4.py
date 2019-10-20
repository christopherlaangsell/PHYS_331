# Template File for Homework 3, Problem 4
# PHYS 331
# Amy Oldenburg

## module newtonRaphson

# has been modified to strip bisection aspects of the code
# is generally UNSAFE, but can be used for specific case of Problem 4
import numpy as np
import matplotlib.pyplot as plt

def newtonRaphsonMOD(f,df,a,b): # YES YOU MAY MODIFY!
    
    from numpy import sign
    
    error = []   #making error list
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
      # Try a Newton-Raphson step    
        dfx = df(x)
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx
        error.append(np.abs((x-dx)-x))     #adding to list of errors
   
    error = np.array(error)    #converting list to array
    print(error)
    return error

x=np.arange(0,15,.01)   
def func(x):
    return (x-10)*(x+25)*(x**2+45)   #OG func

def dfunc(x):
    return 4*x**3+45*x**2-410*x+675            #Derivative

error_array = newtonRaphsonMOD(func,dfunc,0,15)          #putting errors into array


def mfunc(error):                  #finding when xn+1/xn is consistent
    m = []
    for i in range(0,29):
        if(error[i]**2 == 0.0):   #avoiding dividing by 0
            break
        
        try: 
            m.append(error[i+1]/((error[i])**2))       #plugging in m=2
        except RuntimeWarning :
            break
    
    print(m)
    return 
        

mfunc(error_array)

plt.xlabel('x')             #Setting x axis label
plt.ylabel('y')             #Setting y axis label
plt.xlim(0,15)              #Showing x range
plt.ylim(-20,20)
plt.grid(True)              #Putting in gridlines
plt.plot(error_array[:11] ) #Plotting
plt.legend(['error'], loc = 0)     #Making legend best location                  
plt.show()