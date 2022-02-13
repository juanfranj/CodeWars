def get_sum(a,b):
    c=[]
    if a>b:
        for i in range(b,a+1):
            c.append(i)
        return sum(c)
    elif a<b:
        for i in range(a,b+1):
            c.append(i)
        return sum(c)
    elif a==b:
        return a