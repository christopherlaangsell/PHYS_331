#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 09:06:37 2018

@author: christophergsell
"""
import numpy as np
import matplotlib.pyplot as plt


def checkConditioning(tvec):
    A = np.array([[1,tvec[0],0.5*tvec[0]**2],
                    [1, tvec[1], 0.5*tvec[1]**2],
                    [1, tvec[2], 0.5*tvec[2]**2]])
    
    norm = 0
    for i in range(len(A)):
        for j in range(len(A)):
            norm += A[i][j]**2
    normA = np.sqrt(norm)
    return np.abs(np.linalg.det(A))/normA


#part c 
def main1():
    dt = np.arange(.1,5.1,.1)
    Rs =[]
    for d in dt:
        Rs.append(checkConditioning(d*np.array([0,1,2])))
        
    
    
    plt.plot(dt,Rs)
    plt.grid()
    plt.xlabel("dt")
    plt.ylabel('R')
    plt.title('R vs delta t')
    plt.legend()
    plt.show(True)
    
    print('Max R = ' + str(np.max(Rs)))
main1()



#part d
def main2():
    dt = np.arange(0,10,.1)
    Rs = []
    for d in dt:
        Rs.append(checkConditioning(np.array([0,d,10])))
    
    plt.plot(dt, Rs)
    plt.xlabel("t2")
    plt.ylabel('R')
    plt.title('R vs t2')
    plt.grid()
    plt.show(True)
    
    print("Best value of t2 = " + str(dt[np.argmax(Rs)]))
    print('max R = ' + str(np.max(Rs)))
    
main2()

#part e

def solveStrat1():
    A = np.array([[1,0,0],[1,5,12.5],[1,10,50]])
    Xs = np.array([.3,4.425,14.3])
    print("Strategy 1 best fit parameters (x,v,a) " + str(np.linalg.solve(A,Xs)))


def solveStrat2():
   A = np.array([[1,0,0],[1,1,.5],[1,10,50]])
   Xs = np.array([.3,.665,14.3])
   print("Strategy 2 best fit parameters (x,v,a) " + str(np.linalg.solve(A,Xs)))

solveStrat1()
solveStrat2()
'''
def solveStrat3():
    A = np.array([[1,0,0],[1,5,12.5],[1,10,50]])
    Xs = np.array([.3,4.425-.005,14.3-.005])
    print("Strategy 1 Lower best fit parameters (x,v,a) " + str(np.linalg.solve(A,Xs)))

def solveStrat5():
    A = np.array([[1,0,0],[1,5,12.5],[1,10,50]])
    Xs = np.array([.3,4.425+.005,14.3+.005])
    print("Strategy 1 Upper best fit parameters (x,v,a) " + str(np.linalg.solve(A,Xs)))


def solveStrat4():
   A = np.array([[1,0,0],[1,1,.5],[1,10,50]])
   Xs = np.array([.3,.665+.005,14.3+.005])
   print("Strategy 2 Upper best fit parameters (x,v,a) " + str(np.linalg.solve(A,Xs)))

def solveStrat6():
   A = np.array([[1,0,0],[1,1,.5],[1,10,50]])
   Xs = np.array([.3,.665-.005,14.3-.005])
   print("Strategy 2 Lower best fit parameters (x,v,a) " + str(np.linalg.solve(A,Xs)))


solveStrat3()
solveStrat5()
solveStrat4()
solveStrat6()


'''
