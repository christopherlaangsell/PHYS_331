
import numpy as np
import matplotlib.pyplot as plt
import scipy as spy

x = np.arange(-1,1,.01)
z = np.arange(-1,1,.01)

def func4(z):
    return 0.5*((1-z**2)**(1/2))*((np.sqrt(2)-1)**2-(np.sqrt(1+z**2)-1)**2)**(-1/2)

def funcCheb(f,n):
    A = np.pi/(n+1)
    
    
    xs = np.zeros((n+1))
    
    for j in range(n+1):
        xs[j] = np.cos(((2*j+1)*np.pi)/(2*n+2))
        
    return A * np.sum(f(xs))
    
    
def func5(x):
    return ((np.sqrt(2)-1)**2-(np.sqrt(1+x**2)-1)**2)**(-1/2)

exact_solution = spy.integrate.quad(func5,0,1)

print("area exact: ", exact_solution[0])
print('\n')

tol = 1e-6
i=0
error = tol*2

while(error>tol):
    area=funcCheb(func4,i)
    print("Chebyshev area when n = " +str(i) + ":   " + str(area))
    error = np.abs(area-exact_solution[0])
    i += 1
    