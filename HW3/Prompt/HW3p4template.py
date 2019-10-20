# Template File for Homework 3, Problem 4
# PHYS 331
# Amy Oldenburg

## module newtonRaphson

# has been modified to strip bisection aspects of the code
# is generally UNSAFE, but can be used for specific case of Problem 4
def newtonRaphsonMOD(f,df,a,b): # YES YOU MAY MODIFY!
    from numpy import sign
    
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): 
        print('Root is not bracketed')
        return []
    x = 0.5*(a + b)                    
    for i in range(30):
        fx = f(x)
      # Try a Newton-Raphson step    
        dfx = df(x)
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx
    return x

    

