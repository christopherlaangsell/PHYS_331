

import numpy as np
import matplotlib.pyplot as plt

#Question 1

def CreateSystem(kvec,mvec):
    A = np.zeros((len(mvec),len(mvec)))
    
    for i in range(len(mvec)):
        for j in range(len(mvec)):
            if(i==j+1):
                A[i][j] = kvec[i]/mvec[i]
                
            if(i==j):
                A[i][j] = -1*((kvec[j]+kvec[j+1])/mvec[i])
                
            if(i+1==j):
                A[i][j] = kvec[j]/mvec[i]
                
            
            
                
    return(A)

    
def main():
    kvec = np.array([[1.],[1],[1],[1]])
    mvec = np.array([[1.],[1],[1]])
    
    eigval, eigvec = np.linalg.eig(CreateSystem(kvec,mvec))
    
    print(eigval)
    print(eigvec)

    
main()


#Part 2

def main2():
    
    n = 1000
    mass = np.ones((n,1))
    
    for i in range(n):
        if(i % 2 == 0):
            mass[i][0] = 1.5
        else:
            mass[i][0] = 1
            
    Ks = np.ones((n+1,1))
    
    
    values, vectors = np.linalg.eig(CreateSystem(Ks,mass))
    
    plt.hist(values,100)
    plt.show()

    
    
    
main2()

#Part 3

def main3():
    n = 1000
    mass = np.ones((n,1))
    
    for i in range(n):
        if(i % 2 == 0):
            mass[i][0] = 1.2
        else:
            mass[i][0] = 1
            
    Ks = np.ones((n+1,1))
    
    
    values, vectors = np.linalg.eig(CreateSystem(Ks,mass))
    
    plt.hist(values,100)
    plt.show()
    
main3()