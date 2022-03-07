
def zeros(n):          
    number=0        
    while(n):
        number+=int(n/5)
        n=int(n/5)   
    return number
if __name__ == '__main__':
    n = 30
    sol = zeros(n)
    print(sol)
'''
def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0
'''