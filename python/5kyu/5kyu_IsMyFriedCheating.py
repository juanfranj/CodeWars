def remov_nb(n):
    sol = []
    suma =  n * (n+1) // 2
    for i in range(1, n+1):
        aux = (suma - i) / (i+1)
        if aux % 1 == 0 and aux <= n:
            sol.append((i, int(aux)))
           
    return sol



if __name__ == '__main__':
    n = 1000003
    print(remov_nb(n))

