# Template File for Homework 2, Problem 2
# PHYS 331
# Amy Oldenburg
import numpy as np
import matplotlib.pyplot as plt

def rf_bisect(f,xlo,xhi,xtol,nmax):
#Computes the value of the root for function f bracketed in the domain [xlo, xhi]. 
# PARAMETERS:
#   f     --  (function) The one-dimensional function to evaluate a root of.
#   xlo   --  (float) The lower limit of the bracket.
#   xhi   --  (float) The upper limit of the bracket.
#   xtol  --  (float) The tolerance the calculated root should achieve.
#   nmax  --  (int) The maximum number of iterations allowed.

# RETURNS: (tuple(float, int)) A root of f that meets the tolerance tol the number 
# of iteratons required to converge.
    
#----> Implement your solution for rf_bisect here <-------

    return (root, iters)

# Functions f1, f2, f3, and f4 that may be used to test your implementation of rf_bisect.
def f1(x):
    return 3 * x + np.sin(x) - np.exp(x)

def f2(x):
    return x**3

def f3(x):
    return np.sin(1. / (x + 0.01))

def f4(x):
    return 1. / (x - 0.5)


# Example: Find the root of f2(x) and print the result.

#(root,iters) = rf_bisect(f2, -1., 1., 1e-6, 25)
#print('Root of f2: ' + str(root))
#print('# iterations: ' + str(iters))
#fval=f2(root)
#print('f2 evaluated at root is: ' + str(fval))

#----> (Hint: you might consider shortcuts to automate)
# (it's OK if you write additional functions to perform repetitive tasks)



    