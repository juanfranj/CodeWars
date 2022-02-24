def array_diff(a, b):
    
    return [i for i in a if i not in b]

if __name__ == '__main__':
    a = [1,2,3]
    b = [1, 2]
    print(array_diff(a, b))