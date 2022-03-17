from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_div = round(sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = 0
    print(is_prime(n))
