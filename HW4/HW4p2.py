import numpy as np

def f(x,y):
    g1 = 2*x**3-6*y**2*x-1
    g2 = 6*x**2*y-2*y**3+3
    
    return np.array([g1,g2])

def Jinv(x,y):
    det = 1/((6*x**2-6*y**2)**2+(12*x*y)**2)
    return [(6*x**2-6*y**2)*det, (12*x*y)*det],[(-12*x*y)*det,(6*x**2-6*y**2)*det]

def rf_newton2d(f_system, Jinv_system, x0, y0, tol, maxiter):
    prev_x = x0
    prev_y = y0 #initializing
    count = 0 # for iterations
    
    while count<maxiter:
        
        #f_system = f(x0, y0) #using earlier method
        #Jinv_system = Jinv(x0,y0) #using earlier method
        f_current = f(prev_x,prev_y)
        Jinv_current = Jinv(prev_x,prev_y)
        #equation
        next_x = prev_x - ((Jinv_current[0][0]*f_current[0])+(Jinv_current[0][1]*f_current[1]))
        next_y = prev_y - ((Jinv_current[1][0]*f_current[0])+(Jinv_current[1][1]*f_current[1]))
        
        
        delta = ((next_x-prev_x)**2+(next_y-prev_y)**2)**(.5)
        
        prev_x = next_x
        prev_y = next_y
        
        if(delta <= tol):
            break
        
        count = count +1
    return [next_x,next_y]


tol = 10e-5
maxits = 50


#Test

print('Root(1,0) = ' + str(rf_newton2d(f(1,0), Jinv(1,0),1,0,tol,maxits)))
print('Root(-1,0) = ' + str(rf_newton2d(f(-1,0), Jinv(-1,0),-1,0,tol,maxits)))
print('Root(0,1) = ' + str(rf_newton2d(f(0,1), Jinv(0,1),0,1,tol,maxits)))
print('Root(0,-1) = ' + str(rf_newton2d(f(0,-1), Jinv(0,-1),0,-1,tol,maxits)))
print('Root(-1,-1) = ' + str(rf_newton2d(f(-1,-1), Jinv(-1,-1),-1,-1,tol,maxits)))
print('Root(1,1) = ' + str(rf_newton2d(f(1,1), Jinv(1,1),1,1,tol,maxits)))
print('Root(1,-1) = ' + str(rf_newton2d(f(1,-1), Jinv(1,-1),1,-1,tol,maxits)))
print('Root(-1,1) = ' + str(rf_newton2d(f(-1,1), Jinv(-1,1),-1,1,tol,maxits)))
print('Root(0,0) = division by zero')

        
        




