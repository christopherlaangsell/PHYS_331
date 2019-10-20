import numpy as np
import scipy as spi
import matplotlib.pyplot as plt


#part a
def func(x,y):
    return x**2-y**2

matrix = np.zeros((11,11))   #setting zero matrix
xs = np.arange(-1,1.2,.2)
ys = np.arange(-1,1.2,.2)

for row in range(0,11):
    for col in range(0,11):
        matrix[row,col]=func(xs[col],ys[row])  #Filling in
        
        
        
plt.imshow(matrix)
plt.show()


#part b

def bilinear2D(xsamp,ysamp,xdata,ydata,zdata):
    zsamp = np.zeros((len(xsamp),len(ysamp)))    #setting zero matrix
    
    
    
    for col in range(len(xsamp)):
        for row in range(len(ysamp)):
            
            xcoord = int((xsamp[col]/.2)+5) #getting correct index
            ycoord = int((ysamp[row]/.2)+5)
            
            
            t = (xsamp[col]-xdata[xcoord])/(xdata[xcoord+1]-xdata[xcoord])
                
            
            u = (ysamp[row]-ydata[ycoord])/(ydata[ycoord+1]-ydata[ycoord])
            
            z1= func(xdata[xcoord],ydata[ycoord])   #the four surrounding coordinates
            z2= func(xdata[xcoord+1], ydata[ycoord])
            z3= func(xdata[xcoord+1], ydata[ycoord+1])
            z4= func(xdata[xcoord], ydata[ycoord+1])
            zsamp[row,col] = (1-t)*(1-u)*z1+t*(1-u)*z2+t*u*z3+(1-t)*u*z4   #equation
                
            
    
    return zsamp


xsamp = np.arange(-1,1,.01)
ysamp = np.arange(-1,1,.01)
zsamp=bilinear2D(xsamp,ysamp,xs,ys,matrix)

plt.imshow(zsamp)
plt.show()
