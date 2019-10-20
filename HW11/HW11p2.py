
import numpy as np
import matplotlib.pyplot as plt
import random
import time


def myDFT(hk):
    Hn = np.zeros(len(hk), dtype=complex)
    summ = 0 
    
    for i in range(len(hk)):
        
        for k in range(len(hk)):
            summ = summ + hk[k]*np.e**((-1j*2*np.pi*k*i)/len(hk))
        
        Hn[i] = summ
        
    return Hn   


def generatehk(N):
    
    hk = np.zeros((N))
    
    for i in range(N):
        hk[i] = np.random.rand()
    

    return hk

N = 10
hk = generatehk(N)

print(np.fft.fft(hk))
print()
print(myDFT(hk))
print()
print("numpy.fft.fft and myDFT (bottom one) are in agreement")

NNew = 2**np.arange(3,9)
t = np.zeros(len(NNew))


for i in range(len(NNew)):
    time1 = time.time()
    myDFT(generatehk(NNew[i]))
    time2 = time.time()
    t[i] = time2-time1

plt.loglog(NNew,t, label = "Time vs N")
plt.grid(True)
plt.xlabel("N's")
plt.ylabel("Times")
plt.legend()
plt.show()
