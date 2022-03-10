from math import sqrt
def prime_factors(n):
    dic = {}
    primo = 2
    while primo <= n: 
        n, primo = comprueba_factor(n, primo, dic)       
    sol = escribe_factores(dic)
    return sol

def escribe_factores(dic):
    sol = ''
    for key, valor in dic.items():
        if valor == 1:
            sol += f'({key})'
        elif valor > 1:
            sol += f'({key}**{valor})'
    return sol

def comprueba_factor(n,primo, dic):
    if n%primo == 0:
        introduce_factor(primo,dic)
        n //= primo
    else:
        primo = introduce_primo(primo, dic)
    return n, primo

def introduce_primo(primo, dic):
    if primo not in dic.keys():
        dic[primo] = 0
    else:
        primo += 1
    return primo

def introduce_factor(primo, dic):
    if primo not in dic.keys():
        dic[primo] = 1
    else:
        dic[primo] += 1

if __name__ == '__main__':
    n = 25002385
    sol = prime_factors(n)
    print(sol)

'''
def primeFactors(n):
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0: n, j = n / i, j + 1
        if j > 0: p.append([i,j])
        i, j = i + 1, 0
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)


def primeFactors(n):
    i = 2
    r = ''
    while n != 1:
        k = 0
        while n%i == 0:
            n = n / i
            k += 1
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0: pass
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        i += 1
        
    return r


'''