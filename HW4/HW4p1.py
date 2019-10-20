import numpy as np
import matplotlib.pyplot as plt

def g1(x):
    return (x**5-3*x**3+15*x**2+9)/-29
def g2(x):
    return ((x**5-3*x**3+29*x+9)/-15)**(1/2)
def g3(x):
    return (x**6-3*x**4+15*x**3+29*x**2)/-9
    
def dg1(x):
    return (5/-29)*x**4+(9/29)*x**2-(30/29)*x
def dg2(x):
    return (-5*x**4+9*x**2-29)/(2*(15)**(1/2)*(-x**5+3*x**3-29*x-9)**(1/2))
def dg3(x):
    return (-2/3)*x**5+(4/3)*x**3-5*x**2-(58/9)*x
    

#func 1 
x=np.arange(-5,5,.01) #setting mesh size. 
plt.plot(x,g1(x), label = 'Function 1')
plt.plot(x, np.abs(dg1(x)), label = 'Derivative of Function 1')
plt.plot(x, x, label = 'y = x')
plt.plot(x, 0*x, label = 'y=0')
plt.plot(x, 1+0*x, label = 'x=0')
plt.xlabel('x')             
plt.ylabel('y')  
plt.title('Function 1')      
plt.xlim(-5,5) 
plt.ylim(-5,5)            
plt.grid(True)
plt.legend( loc = 0)     #Making legend best location                  
plt.show()  

#func 2 
x=np.arange(-5,5,.01) #setting mesh size. 
plt.plot(x,g2(x), label = 'Function 2')
plt.plot(x, np.abs(dg2(x)), label = 'Derivative of Function 2')
plt.plot(x, x, label = 'y = x')
plt.plot(x, 0*x, label = 'y=0')
plt.plot(x, 1+0*x, label = 'x=0')
plt.xlabel('x')             
plt.ylabel('y')  
plt.title('Function 2')      
plt.xlim(-5,5) 
plt.ylim(-5,5)            
plt.grid(True)
plt.legend( loc = 0)     #Making legend best location                  
plt.show()  

#func 3 
x=np.arange(-5,5,.01) #setting mesh size. 
plt.plot(x,g3(x), label = 'Function 3')
plt.plot(x, np.abs(dg3(x)), label = 'Derivative of Function 3')
plt.plot(x, x, label = 'y = x')
plt.plot(x, 0*x, label = 'y=0')
plt.plot(x, 1+0*x, label = 'x=0')
plt.xlabel('x')             
plt.ylabel('y')  
plt.title('Function 3')      
plt.xlim(-5,5) 
plt.ylim(-5,5)            
plt.grid(True)
plt.legend( loc = 0)     #Making legend best location                  
plt.show()  



#Part c

def fixed_pt(g,xstart,tol):
    x = g(xstart)
    dif = (xstart-x)/2
    while dif > tol:
        x = g(xstart)
        dif = (xstart-x)/2
        xstart = x
    return (x)




#part d
    
print('Roots of Function 1')
print('root 1 is ' + str(fixed_pt(g1,-2,10e-20)))
print('root 2 is ' + str(fixed_pt(g1,-1,10e-20)))
print('root 3 is ' + str(fixed_pt(g1,-0,10e-20)))
print('\n')

print('Roots of Function 2')
print('Not Found')
print('\n')

print('Roots of Function 3')
print('root 1 is ' + str(fixed_pt(g3,-1.5,10e-20)))
print('root 2 is ' + str(fixed_pt(g3,-2,10e-20)))
print('root 3 is ' + str(-1*fixed_pt(g3,0,10e-20)))

