def fit_in(a, b, m, n):
    return (a+b) <= m and max([a,b]) <=n or (a+b) <= n and max([a,b]) <= m


if __name__ == '__main__':
    a , b, m, n = (7,1,7,8)
    print(fit_in(a , b, m, n))
'''
def fit_in(a, b, m, n):
  return max(a, b) <= min(m, n) and a + b <= max(m, n)
'''