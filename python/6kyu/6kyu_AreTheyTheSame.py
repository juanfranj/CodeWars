def comp(array1, array2):
    if array1 == None or array2 == None or len(array1) != len(array2):
        return False 
    array1.sort(key=abs)
    array2.sort(key=abs)
    return all(a**2 == b for a, b in zip(array1, array2))

if __name__ == '__main__':
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    print(comp(a1, a2))

'''
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

'''