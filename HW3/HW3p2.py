import numpy as np
import matplotlib.pyplot as plt




def func(x):
    return x**5-(3*x**3)+(15*x**2)+29*x+9

def deriv(x):
    return 5*x**4-9*x**2+30*x+29
def second_deriv(x):
    return 20*x**3-18*x+30







def Newt(xstart, tol):
    current = xstart
    xn1 = xstart-func(xstart)/deriv(xstart)   #iteration equation
    count = 1
    
    
    while tol<np.abs(current - xn1):
        current = xn1
        xn1 = current-func(current)/deriv(current)    #looping through iteration until reaching tolerance
        count += 1
    
    error = np.float64(np.abs(current-xn1))   #put in float64 to try and show more detail
    print(error)
    return xn1



a = np.float64(Newt(2, 10**-20))       # find root
print(a)
    



def dg(x):
    return np.abs((func(x)*second_deriv(x))/(deriv(x))**2)    #when is it converging
 
    

x=np.arange(-10,10,.01)
plt.xlabel('x')             #Setting x axis label
plt.ylabel('y')             #Setting y axis label
plt.xlim(-4,4)              #Showing x range
plt.ylim(-.5,4.5)
plt.grid(True)              #Putting in gridlines
plt.plot(x, func(x)) #Plotting
plt.plot(x, dg(x)) 
plt.plot(x,1+0*x)
plt.plot(x,0*x)
plt.legend(['func(x)'], loc = 0)     #Making legend best location                  
plt.show()
