#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 15:02:29 2018

@author: christophergsell
"""

import numpy as np

def triSolve(M,b, upperOrLower):
    
    l = len(M)
    xv = np.zeros((l,1))
    if upperOrLower == 0:
        xv[0][0] = b[0][0]/M[0][0]
        for i in range(1,len(M)):
            xv[i][0] = (b[i][0]-dot(M[i][0:i],xv[0:i]))/M[i][i]
        
    else:
        xv[l-1][0] = b[l-1][0]/M[l-1][l-1]
        for i in range(l-2,-1,-1):
            xv[i][0] = (b[i][0]-dot(M[i][i+1:l],xv[i+1:l]))/M[i][i]
    return xv    

def checkSolve(M,x,b):
    return np.dot(M,x)-b
            
            
            
def dot(v1,v2):
    rdot = 0
    for i in range(len(v1)):
        rdot += v1[i]*v2[i][0]
    return rdot





def generateMatrix(n):
    A = np.random.random((n,n))
    for row in range(1,n):
        for col in range(row):
            A[row][col] = 0
            
    return A

def generate_b(n):
    b = np.zeros((n,1))
    for row in range(n):
        b[row][0] = np.random.random()
    return b

def main():
    M = np.array([[9,0,0],[-4,2,0],[1,0,5]])
    b = np.array([[8],[1],[4]])
    x = triSolve(M,b,0)
    r = checkSolve(M,x,b)
    print(r)
    print('\n')
    
    
    b3 = generate_b(3)
    b10 = generate_b(10)
    b30 = generate_b(30)
    b100 = generate_b(100)
    
    M3 = generateMatrix(3)
    M10 = generateMatrix(10)
    M30 = generateMatrix(30)
    M100 = generateMatrix(100)
    
    x3 = triSolve(M3, b3, 1)
    x10 = triSolve(M10, b10, 1)
    x30 = triSolve(M30, b30, 1)
    x100 = triSolve(M100, b100, 1)
    
    r3 = checkSolve(M3, x3, b3)
    r10 = checkSolve(M10, x10, b10)
    r30 = checkSolve(M30, x30, b30)
    r100 = checkSolve(M100, x100, b100)
    
    print('n=3, '+ 'error: ' + str(np.sum(np.abs(r3))))
    print('n=10, ' + 'error: ' + str(np.sum(np.abs(r10))))
    print('n=30, '+ 'error: ' + str(np.sum(np.abs(r30))))
    print('n=100, '+ 'error: ' + str(np.sum(np.abs(r100))))
    
main()