def dbl_linear(n):
    aux = [1]
    cont = 0
    while cont < 10*n:
        y = 2*aux[cont]+1
        z = 3*aux[cont]+1 
        aux.append(y)
        aux.append(z)
        cont += 1
        
    sol = sorted(list({i for i in aux}))
    print(f"n= {n} a[{n}]= {sol[n]}")
    print(sol.index(1511311))
    return sol[n]

if __name__ == '__main__':
    n = 60000
    sol = dbl_linear(n)
    print(sol)

'''
from collections import deque

def dbl_linear(n):
    u, q2, q3 = 1, deque([]), deque([])
    for _ in range(n):
        q2.append(2 * u + 1)
        q3.append(3 * u + 1)
        u = min(q2[0], q3[0])
        if u == q2[0]: q2.popleft()
        if u == q3[0]: q3.popleft()
    return u
'''