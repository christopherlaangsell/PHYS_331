# HW7 Problem 2 template file -- Christopher Gsell

#--Do not modify below this line--#
import numpy as np

# this function inputs an nxn matrix "Ain" and an nx1 column matrix "bin"
# it performs Gauss elimination and outputs the eliminated new matrices
# "A" is also nxn upper triangular, and "b" as an nx1 column matrix
def GaussElimin(Ainput,binput):
    n=len(binput)
    A = Ainput.copy() # make copies so as not to write over originals
    b = binput.copy()
    # loop over pivot rows from row 1 to row n-1 (i to n-2)
    for i in range(0,n-1):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1,n):
            c = A[j,i]/A[i,i] # multiplicative factor to zero point
            A[j,i] = 0.0 # we know this element goes to zero
            A[j,i+1:n]=A[j,i+1:n]-c*A[i,i+1:n] # do subtraction of two rows
            b[j] = b[j]-c*b[i] # do substraction of b's as well
    return (A,b)  # return modified A and b

#---Do not modify above this line--#
    
#part b
def main():
    Ainput = np.array([[4.,-2,1],[-3,-1,4],[1,-1,3]])  #Test Matrix. Important to make these floats
    binput = np.array([[15.],[8],[13]])  #b column matrix, important to make this column oriented
    
    G = GaussElimin(Ainput,binput)
    
    A1 = G[0]  #Because Gauss Elimin returns a tuple, you need to assign each element to a new variable
    b1 = G[1]


    print(triSolve(A1,b1, 1))  #Here, I use the old code I made last week to solve the row reduced matrix.
#Print statement equals the x provided. Check.
#x = np.array([2,-2,3]) This should be the answer
main()
def dot(v1,v2):
    rdot = 0
    for i in range(len(v1)):
        rdot += v1[i]*v2[i][0]
    return rdot

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



#part c

def main2():
    Ainput = np.array([[2,2,3,2],[0.,2,0,1],[4,-3,0,1],[6,1,-6,-5]]) # In this case, 
    #the first and second rows have been swapt
    binput = np.array([[-2],[0.],[-7],[6]]) #Because first and second rows of A input were swapped,
    #the first and second rows of this column vector were also swapped
    
    G = GaussElimin(Ainput,binput)
    
    A1 = G[0]
    b1 = G[1]
    
    print('\n') #space for clarity
    print(triSolve(A1,b1,1)) #same as part b
    
main2()

#This should return x2 = -.5,1,1/3,-2