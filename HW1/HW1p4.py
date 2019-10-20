#Christopher Gsell





def fib_loop(n):
    n0 = 0
    n1 = 1
    for i in range(0,n+1):              #Has to be n+1 because Fn begins at 0
        if i == 0 :
            Fn = n0                  
            
        elif i == 1:
            Fn = n1
        
        else:
            Fn = n1+n0
            n0 = n1
            n1 = Fn
            
            
    
    return Fn



def fib_recur(n):                   #This recursive is calling itself until
                                    # it stops at n == 0
    if n == 0: 
        return 0
    elif n==1:
        return 1
    else:
        Fn = fib_recur(n-1)+fib_recur(n-2)
        
        return Fn
    

