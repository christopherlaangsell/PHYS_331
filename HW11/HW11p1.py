
import numpy as np
import matplotlib.pyplot as plt

def funcSawtooth(kmax):
    #A0/2+sum(Ak*cos((pi*k*x)/L) +Bk*sin((pi*k*x)/L)) this is the equation
    
    mesh = 1/(100*kmax) #mesh dependancy, as frequency goes up, need a smaller mesh
    
    A0 = 1  #determined in written part
    ksum = 0  #initialize
    x = np.arange(-1,1,mesh)   #mesh of x
    
    for k in range(1,kmax+1,1):
        Ak = 0 #setting initials
        Bk = 0
        
        if(k%2 == 0):  #If even
            Ak = 0
            
        else:
            Ak = 4/((np.pi**2)*(k**2))  #If odd
           
            
        ksum = ksum + Ak*np.cos((np.pi*k*x)/1)+Bk*np.sin((np.pi*k*x)/1)  #summation
    
    fx = (A0/2)+ksum
    
    
    
    og = -1*np.abs(x)+1  #original equation
    
    plt.plot(x,fx, label = "Fourier series approximation")
    plt.plot(x,og, label = "Original Sawtooth Function")
    plt.grid(True)
    plt.legend()
    plt.title("Kmax = " + str(kmax))
    plt.show()
    

def main():
    
    funcSawtooth(1)
    funcSawtooth(2)
    funcSawtooth(3)
    funcSawtooth(30)


main()


#----------------------
#Part D

def ModFuncSawtooth(kmax):
    
    mesh = 1/(100*kmax) #mesh dependancy, as frequency goes up, need a smaller mesh
    
    A0 = 1  #determined in written part
    ksum = 0  #initialize
    x = np.arange(-3,3,mesh)   #mesh of x
    
    for k in range(1,kmax+1,1):
        Ak = 0 #setting initials
        Bk = 0
        
        if(k%2 == 0):  #If even
            Ak = 0
            
        else:
            Ak = 4/((np.pi**2)*(k**2))  #If odd
           
            
        ksum = ksum + Ak*np.cos((np.pi*k*x)/1)+Bk*np.sin((np.pi*k*x)/1)  #summation
    
    fx = (A0/2)+ksum
    
    
    
    
    
    plt.plot(x,fx, label = "Extended Fourier series approximation")
    plt.grid(True)
    plt.legend()
    plt.title("Kmax = " + str(kmax))
    plt.show()
    
def main2():
    
    print("*****Part D*****")
    ModFuncSawtooth(1)
    ModFuncSawtooth(3)
    ModFuncSawtooth(30)
  


main2()