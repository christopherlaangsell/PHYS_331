
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
def func2(x):
    return np.sqrt(1-x**2)
    
def func3(x):
    return 2*x**2*np.sqrt(2-x**2)

plt.plot(x, func2(x), label = 'Unmodified Function')
plt.plot(x, func3(x), label = 'Substituted Function')
plt.grid(True)
plt.legend()
plt.show()

def SimpsonIntegrate(f,a,b,n):
    
    
    while(n%6 != 1):
        n = n+1
        
    h = (b-a)/(n-1)
   
    print('n = ' + str(n))
    x = np.linspace(a,b,n)
    summ = 0
    for i in range(1,n-1,1):
        summ = summ + f(x[i])
     
    
    trap = (h/2)*(f(x[0])+f(x[n-1]))+h*summ
    
    #trap = (h/2)*(f(x[0])+f(x[n-1]))+ h*np.sum(f(x[1:n-1]))

    
    

    sum1 = 0
    for i in range(1,n,2):
        sum1 = sum1+f(x[i])
    
    sum2 = 0
    for i in range(2,n-1,2):
        sum2 = sum2 +f(x[i])
            
    simp1 = (h/3)*(f(x[0])+4*sum1+2*sum2+f(x[n-1]))
    
    sum11 = 0
    for i in range(1,n,3):
        sum11 = sum11 + f(x[i])
    
    
    sum12 = 0
    for i in range(2,n-1,3):
        sum12 = sum12 + f(x[i])
        
        
    sum13 = 0
    for i in range(3,n-2,3):
        sum13 = sum13 + f(x[i])
        
    simp2 = ((3*h)/8)*(f(x[0])+3*sum11+3*sum12+2*sum13+f(x[n-1]))
    
    return(trap,simp1,simp2)
    
func2si = SimpsonIntegrate(func2,0,1,10**3)
func3si = SimpsonIntegrate(func3,0,1,10**3)

solu = np.pi/4

print('\n')
print('Unmodified Function')
print('Trapezoid error')
print(np.abs(func2si[0]-solu))
print('Simpson 1/3 error')
print(np.abs(func2si[1]-solu))
print('Simpson 3/8 error')
print(np.abs(func2si[2]-solu))
print('\n')
print('Substituted Function')
print('Trapezoid error')
print(np.abs(func3si[0]-solu))
print('Simpson 1/3 error')
print(np.abs(func3si[1]-solu))
print('Simpson 3/8 error')
print(np.abs(func3si[2]-solu))