#Christopher Gsell

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-5,6,.01) #setting mesh size. If mesh size > 2, too course

plt.xlabel('x')             #Setting x axis label
plt.ylabel('y')             #Setting y axis label
plt.xlim(-5,5)              #Showing x range
plt.grid(True)              #Putting in gridlines

def plot_tanh():
    plt.plot(x, np.tanh(x), 'o-') #Plotting 
    plt.legend(['tanh(x)'], loc = 0)     #Making legend best location                  
    plt.show()                  #Showing plot
    
def plot_tanh2(a):
    for i in range(0,3):    #For loop to plot each of three curves
        plt.plot(x, np.tanh(x*a[i]))
    plt.legend(['tanh(.5x)','tanh(1.3x)', 'tanh(2.2x)'], loc =0)
    plt.show()
    
def main_b():
    a=[.5,1.3,2.2]
    plot_tanh2(a) # calling plot_tanh2 using local variable a
    
    
plot_tanh()        #Calling methods
main_b()






