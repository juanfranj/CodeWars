def dig_pow(n, p):
    suma = 0
    exp = p
    for i in str(n):
        suma += int(i)**exp
        exp += 1
    print(suma)
    return suma//n if suma >= n and suma%n == 0 else -1

if __name__ == '__main__':
    n = 46288
    p = 5
    print(dig_pow(n,p))
    for i,c in enumerate(str(n)):
        print(i,c)

'''
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1
'''