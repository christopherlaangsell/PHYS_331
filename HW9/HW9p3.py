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
 
    
    
def MatrixA():
    A = np.zeros((9,9))
    for y in range(9):
        for x in range(9):
            if(y == x):
                A[y][x] = -4
            
            if((y == x+1) and y != 3 and y!= 6):
                A[y][x] = 1
            
            if((x == y+1) and y != 2 and y!= 5):
                A[y][x] = 1
                
            if(x == y+3 ):
                A[y][x] = 1
            
            if(y == x+3):
                A[y][x] = 1
            
    return A

b = -1*np.array([[0.],[0],[100],[0],[0],[100],[200],[200],[300]])

n, temps = myJacobi(MatrixA(), b, 1, 10**-4)

print(temps)


#Extra credit


def MatrixB():
    B = np.zeros((100,100))
    for y in range(100):
        for x in range(100):
            if(y == x):
                A[y][x] = -4
            
            if((y == x+1) and y != 3 and y!= 6):
                A[y][x] = 1
            
            if((x == y+1) and y != 2 and y!= 5):
                A[y][x] = 1
                
            if(x == y+3 ):
                A[y][x] = 1
            
            if(y == x+3):
                A[y][x] = 1
            
    return A
