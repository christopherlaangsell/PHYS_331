
import numpy as np
import matplotlib.pyplot as plt

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
    
def func1(x):
    if(x ==0):
        return 1
    else:
        return ((np.log(1+x))/x)
    

n = np.array([10,30,100,300,1000,3000,10**4,3*10**4,10**5])

I1 = np.zeros((len(n)))
I2 = np.zeros((len(n)))
I3 = np.zeros((len(n)))

solu = np.pi**2/12

e1 = np.zeros((len(n)))
e2 = np.zeros((len(n)))
e3 = np.zeros((len(n)))


for i in range(len(n)):
     I1[i],I2[i],I3[i] = SimpsonIntegrate(func1,0,1,n[i])
    
    

for i in range(len(n)):
    e1[i] = np.abs(I1[i]-solu)
    e2[i] = np.abs(I2[i]-solu)
    e3[i] = np.abs(I3[i]-solu)



xmesh = np.arange(0,1,.001)
y=np.zeros(len(xmesh))

for i in range(len(xmesh)):
    y[i] = func1(xmesh[i])


plt.plot(xmesh, y, label = 'Given Integrand')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(np.log(n),np.log(e1), label = 'Trapezoidal')
plt.plot(np.log(n),np.log(e2), label = 'Simpsons 1/3')
plt.plot(np.log(n),np.log(e3), label = 'Simpsons 3/8')
plt.grid(True)
plt.xlabel('log of n')
plt.ylabel('log of error')
plt.legend()
plt.show()