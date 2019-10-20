#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 17:39:09 2018

@author: christophergsell
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

        






def ModelSpectrum(c1,c2,v01,v02,g1,g2,v):
    L1 = (1/np.pi)*((1/2)*g1)/((v-v01)**2+(.5*g1)**2)
    L2 = (1/np.pi)*((1/2)*g2)/((v-v02)**2+(.5*g2)**2)
    return c1*L1+c2*L2




def ModelSpectrum2(x,v):
    L1 = (1/np.pi)*((1/2)*x[4])/((v-x[2])**2+(.5*x[4])**2)
    L2 = (1/np.pi)*((1/2)*x[5])/((v-x[3])**2+(.5*x[5])**2)
    return x[0]*L1+x[1]*L2

def Residuals(x,v,Sv):
    return Sv - ModelSpectrum2(x,v)

def main():
    arr = np.loadtxt("HW6p1data.csv", dtype = np.float64, delimiter = ',')
    
    v = np.zeros(len(arr))
    Sv = np.zeros(len(arr))
    
    for i in range(len(arr)):
        v[i] = arr[i][0]
        Sv[i] = arr[i][1]    
    
    x0 = np.array([5,3,20250,20550,40,60])
    
    res = sp.optimize.leastsq(Residuals, x0, args=(v,Sv))
    x1 = res[0]
    
    vmesh = np.arange(20000,21000,.01)
     
    print(x1)
    
    #part b
    plt.plot(v,Sv, 'o',label = 'raw data')
    plt.grid(True)
    plt.title('Part B')
    plt.legend()
    plt.show(True)
    
    #part c
    plt.plot(v,Sv, 'o', label = 'data')
    plt.title('Part C')
    plt.plot(v,ModelSpectrum(2,1,20250,20550,80,90,v), label = 'mspec')
    plt.grid(True)
    plt.legend()
    plt.show(True)
    
    
    #part d
    plt.plot(v,Sv, 'o', label = 'data')
    plt.title('Part D')
    plt.plot(v,ModelSpectrum(2,1,20250,20550,80,90,v), label = 'mspec')
    plt.plot(v,ModelSpectrum2(x0,v), label = 'mspec2')
    plt.grid(True)
    plt.legend()
    plt.show(True)
    
    #part e
    plt.plot(v,Sv,'o', label = 'data')
    plt.title('Part E')
    plt.plot(v,ModelSpectrum2(x0,v), label = 'mspec2')
    plt.plot(v,Residuals(x0,v,Sv), label = 'residual')
    plt.grid(True)
    plt.legend()
    plt.show(True)
    
    
    #culmination
    plt.title('Part H')
    plt.plot(v,Sv, 'o', label = 'data')
    plt.plot(vmesh,ModelSpectrum2(x1,vmesh), label = 'mspec2optimized')
    plt.plot(v,Residuals(x1,v,Sv), label = 'minimzd residual')
    plt.legend()
    plt.grid(True)
    plt.show(True)
    
main()