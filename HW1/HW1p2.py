#Christopher Gsell



def factorial(n):                   #calculating factorial function for later
    if n== 0:
        return 1
    else:
        return n* factorial(n-1)  #recursive
    
def taylor_sin(x0,n):
    if n%2 == 0:        #returning 0 for all even n's
        yn = 0
    elif n<0 :
        return "can't be negative"
    else:
        if (n+1)%4 == 0:        #addressing positive and negative. 
            yn = (-1*x0**n)/factorial(n) #negatives are divisible by 4 if added by 1
        else:
            yn = x0**n/factorial(n)             #any non-negatives are positive
            
        
    return yn
    
        


