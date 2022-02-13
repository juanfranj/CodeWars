def digital_root(n):   
    n=str(n)
    a=0
    for i in n:
        a=a+int(i)
    b=0
    a=str(a)
    if len(a)>1:
        for i in a:
            b=b+int(i)
    else:
        b=a    
    return int(b)