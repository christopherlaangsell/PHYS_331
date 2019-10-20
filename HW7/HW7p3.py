#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 22:32:49 2018

@author: christophergsell
"""

#--Do not modify below this line--#
import numpy as np

# this function inputs an nxn matrix "Ain" and an nx1 column matrix "bin"
# it performs Gauss elimination and outputs the eliminated new matrices
# "A" is also nxn upper triangular, and "b" as an nx1 column matrix
def LUdecomp(Ainput):
    n=len(Ainput)
    L = np.zeros((n,n))
    A = Ainput.copy() # make copies so as not to write over originals
    
    # loop over pivot rows from row 1 to row n-1 (i to n-2)
    for i in range(n):
        L[i][i] = 1
        
    for i in range(0,n-1):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1,n):
            c = A[j,i]/A[i,i] # multiplicative factor to zero point
            A[j,i] = 0.0 # we know this element goes to zero
            L[j][i] = c
            A[j,i+1:n]=A[j,i+1:n]-c*A[i,i+1:n] # do subtraction of two rows
            #b[j] = b[j]-c*b[i] # do substraction of b's as well
    return (L,A)  # return modified A and b

#---Do not modify above this line--#
    
def main1():
    A1 = np.array([[4.,-2,1],[-3,-1,4],[1,-1,3]])
   
    L = LUdecomp(A1)[0]
    U = LUdecomp(A1)[1]
    
    print(np.dot(L,U))
    print(A1)
main1()

def main2():
    A2 = np.array([[2.,2,3,2],[0.,2,0,1],[4,-3,0,1],[6,1,-6,-5]])
    
    L = LUdecomp(A2)[0]
    U = LUdecomp(A2)[1]
    
    print('\n') #spacing
    print('dot of A2 ' + str(np.dot(L,U)))
    print('\n') #spacing
    print('A2 ' +str(A2))
main2()