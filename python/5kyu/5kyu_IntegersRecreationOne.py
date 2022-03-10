from math import sqrt
def list_squared(m, n):
    sol = []
    for i in range(m, n+1):
        div = [j*j for j in range(1, i//2 + 1) if i%j==0]
        sq_divs = sum(div)
        sq_divs += i * i 
        if ((sq_divs) ** 0.5) % 1 == 0:
            sol.append([i, sq_divs])
    return sol

if __name__ == '__main__':
    m = 791
    n = 5245
    sol = list_squared(m,n)
    print(sol)
    
''' 
CACHE = {}

def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number] 
    
    return CACHE[number]

def list_squared(m, n):
    ret = []

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            ret.append([number, divisors_sum])

    return ret

'''