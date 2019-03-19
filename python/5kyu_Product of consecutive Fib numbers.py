def productFib(prod):
    fib=[0,1]
    for i in range(2,200): fib.append(fib[i-2]+fib[i-1])
    for i in range(len(fib)-1): 
        if (fib[i]*fib[i+1])==prod: return [fib[i],fib[i+1],True]
    for i in range(len(fib)-1): 
        if (fib[i]*fib[i+1])>prod: return [fib[i],fib[i+1],False]