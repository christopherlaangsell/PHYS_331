import numpy as np


def main():
    m = np.array([[10.],[4],[5],[6]])
    A = np.array([[m[0][0],1.,0,0],[m[1][0], -1, 1, 0],[m[2][0],0,-1,1],[m[3][0],0,0,-1]])
    u = np.array([[.25],[.3],[.2]])
    g = 9.82
    theta = np.pi/4
    
    b1 = m[0][0]*g*(np.sin(theta)-u[0][0]*np.cos(theta))
    b2 = m[1][0]*g*(np.sin(theta)-u[1][0]*np.cos(theta))
    b3 = m[2][0]*g*(np.sin(theta)-u[2][0]*np.cos(theta))
    b4 = -m[3][0]*g
    
 
    
    b = np.array([[b1],[b2],[b3],[b4]])
    
    x = np.linalg.solve(A,b)
    
    print(x)
    
main()