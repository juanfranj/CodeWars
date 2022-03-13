fibonacci_cache = {}

def fibonacci(input_value):
    if input_value in fibonacci_cache:
        return fibonacci_cache[input_value]
    if input_value == 1:
            value = 1
    elif input_value == 2:
            value = 1
    elif input_value > 2:           
            value =  fibonacci(input_value -1) + fibonacci(input_value -2)
    fibonacci_cache[input_value] = value
    return value

if __name__ == '__main__':
    n = 250
    print(fibonacci(n))

'''
def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
'''
