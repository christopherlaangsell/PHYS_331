import numpy as np
import scipy as spi
import matplotlib.pyplot as plt


#lnspace

def func(x):
    return np.abs(np.sin(x))

x = np.arange(-10,10,.1)
xmesh2 = np.arange(-.5,.5,.001)  #finer mesh

plt.plot(x,func(x))
plt.plot(x, x*0)
plt.ylim(-.1,1.0)
plt.xlim(-10,10)
plt.title('Original Function')
plt.show()

near = spi.interpolate.interp1d(x,func(x),kind='nearest')
lin = spi.interpolate.interp1d(x,func(x), kind='linear')
quad = spi.interpolate.interp1d(x,func(x),kind='quadratic')
cub= spi.interpolate.interp1d(x,func(x),kind='cubic')


#part c

plt.plot(x,func(x),'o', label='support points') 
plt.plot(xmesh2,func(xmesh2), label = 'func_finemesh')                   
plt.plot(x, x*0, label = 'y=0')
plt.plot(xmesh2,near(xmesh2), label = 'interp_nearest')
plt.ylim(-.1,.6)
plt.xlim(-.5,.5)
plt.legend()
plt.title('Nearest Interpolation')
plt.show(True)

plt.plot(x,func(x),'o', label = 'support points')
plt.plot(xmesh2,func(xmesh2), label = 'func_finemesh')
plt.plot(x, x*0, label = 'y=0')
plt.plot(xmesh2,lin(xmesh2), label = 'interp_linear')
plt.ylim(-.1,.6)
plt.xlim(-.5,.5)
plt.legend()
plt.title('Linear Interpolation')
plt.show(True)

plt.plot(x,func(x),'o', label = 'support points')
plt.plot(xmesh2,func(xmesh2), label = 'func_finemesh')
plt.plot(x, x*0, label = 'y=0')
plt.plot(xmesh2,quad(xmesh2),label = 'interp_quadratic')
plt.ylim(-.1,.6)
plt.xlim(-.5,.5)
plt.legend()
plt.title('Quadratic Interpolation')
plt.show(True)

plt.plot(x,func(x),'o', label = 'support points')
plt.plot(xmesh2,func(xmesh2), label = 'func_finemesh')
plt.plot(x, x*0, label = 'y=0')
plt.plot(xmesh2,cub(xmesh2), label = 'interp_cubic')
plt.ylim(-.1,.6)
plt.xlim(-.5,.5)
plt.legend()
plt.title('Cubic Interpolation')
plt.show(True)




#part d

xmesh3 = np.arange(1,2,.001) #encloses pi/2
plt.plot(x,func(x),'o', label = 'support points')
plt.plot(xmesh3, func(xmesh3), label = 'func_finemesh')
plt.plot(x,x*0, label = 'y=0')
plt.plot(xmesh3,lin(xmesh3), label = 'interp_linear')
plt.plot(xmesh3,cub(xmesh3), label = 'interp_cubic')
plt.ylim(.96,1.01)
plt.xlim(1.3,1.85)
plt.legend()
plt.grid(True)
plt.title('Span where cubic interpretation is best')
plt.show(True)