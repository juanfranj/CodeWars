def even_or_odd(number):
    sol = "Even"
    if number % 2:
        sol = "Odd"
    return sol
    

if __name__ == '__main__':
    num = 1
    print(even_or_odd(num))


'''
def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'
'''