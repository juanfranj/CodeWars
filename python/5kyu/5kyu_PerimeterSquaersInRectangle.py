def perimeter(n):
    return 4 * fibonacci(n+1)

def fibonacci(n):
    fib = []
    for num in range(n+1):
        if num == 0:
            fib.append(0)
        elif num == 1:
            fib.append(1)
        else:
            fib.append(fib[-1] + fib [-2])
    return sum(fib[1::])

if __name__ == '__main__':
    n = 90273
    sol = perimeter(n)
    print(sol)

'''
def fib(n):
    a, b = 0, 1

    for i in range(n+1):
        if i == 0:
            yield b 
        else:
            a, b = b, a+b
            yield b
        

def perimeter(n):
    return sum(fib(n)) * 4

'''