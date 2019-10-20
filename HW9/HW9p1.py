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
    
    
    delta = lambda x,x1 : np.amax(np.abs(x-x1)) 
    
    n = 1
    while(delta(x,x1)>tol):
        x = x1
        x1 = np.dot(w,(-np.dot(np.dot(Dinv,L+U),x)+np.dot(Dinv,b)))+np.dot((1-w),x)
        n += 1
    
              
    return(n,x1)
 
    
A1 = np.array([[1.01, .99],[.99, 1.01]])
b1 = np.array([[2.0],[2.0]])

A2 = np.array([[1.5, .5], [.5, 1.5]])
b2 = np.array([[2.0],[2.0]])

A3 = np.array([[9.,10,2],[1,6,3],[10,-1,2]])
b3 = np.array([[7.],[8],[1]])

print(myJacobi(A3,b3,.4,10**-4))
print(np.linalg.solve(A3,b3))


wmesh = np.arange(.01,.33,.01)
nmesh = np.zeros(len(wmesh))

for i in range(len(wmesh)):
    n, x = myJacobi(A3,b3,wmesh[i],10**-4)
    nmesh[i] = n

plt.plot(wmesh,nmesh,'-')
plt.grid(True)
plt.xlabel("relaxation")
plt.ylabel("iterations")
