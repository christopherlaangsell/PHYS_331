import numpy as np
import matplotlib.pyplot as plt


def myJacobi(A,b,w,tol):
    
    s = len(A)
    
    L = np.zeros((s,s))
    U = np.zeros((s,s))
    D = np.zeros((s,s))
    
    
    for i in range(s):
        for j in range(s):
            if(i == j):
                D[i][j] = A[i][j]
            if(j>i):
                U[i][j] = A[i][j]
            if(i>j):
                L[i][j] = A[i][j]
                
            
    Dinv = np.zeros((s,s))
    
    for i in range(s):
        Dinv[i][i] = 1/D[i][i]

    x = np.zeros((s,1))
    
    for i in range(s):
        x[i] = b[i]/A[i][i]
   
    x1 = np.dot(w,(-np.dot(np.dot(Dinv,L+U),x)+np.dot(Dinv,b)))+np.dot((1-w),x)
    delta=np.max(np.abs(x1-x))
    x = x1
    
    #delta = lambda x,x1 : np.amax(np.abs(x-x1)) 
    
    n = 1
    while(delta>tol):
        x1 = np.dot(w,(-np.dot(np.dot(Dinv,L+U),x)+np.dot(Dinv,b)))+np.dot((1-w),x)
        delta=np.max(np.abs(x1-x))
        x=x1
        n += 1
    
              
    return(n,x1)
 
    
def matrixA():
    n = 100
    A = np.zeros((n,n))
    for i in range(n):
        
        if(i<n-1):
            A[i][i+1] = 1
        A[i][i] = -2
        
        if(i>0):
            A[i][i-1] = 1
            
            
    A[0][n-1]=1
    A[n-1][0]=1
    
    return A

def vectorb(x):
    n = 100
    b = np.zeros((n,1))
    for i in range(n):
        b[i][0] = -4*np.pi*np.sin(x[i])
    return b
        
w = 1
tol = 10**-4
x = np.linspace(0,2*np.pi,100)
h=x[1]-x[0]
A=matrixA()/h**2
b=vectorb(x)
iters, phi = myJacobi(A,b,w,tol)
phi_ana = 4*np.pi*np.sin(x)

plt.plot(x,phi, label = 'phi')
plt.plot(x,phi_ana, label = 'phi theoretical')
plt.plot(x, 0*x)
plt.grid(True)
plt.legend()

     