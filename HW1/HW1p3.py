#Christopher Gsell


def maskn(lst, i):          #very important that it's lst and not 1st
    outlist = []            #^took me a hot minute debugging that one
    for k in range(0,len(lst)):
        if lst[k]%i != 0:       
            outlist.append(0)
        else:
            outlist.append(1)
        
    
    return outlist
