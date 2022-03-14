def persistence(n):
    ciclo = 0
    while len(str(n)) > 1:
        mul = 1
        #print(n)
        for i in str(n):
            mul *= int(i)
            n = mul
        ciclo += 1   
    return ciclo

if __name__ == '__main__':
    n = 25
    print(persistence(n))

''' 
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

'''