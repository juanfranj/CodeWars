import collections

def count(a, t, x):

    dic = collections.Counter(a)
    sum = t
    cont = 0
    if sum in dic.keys():
            cont += dic[sum]

    while sum < max(a) and x != 0:
        sum += abs(x) 
        if sum in dic.keys():
            cont += dic[sum]
 
    sum = t
    while sum > min(a) and x != 0:
        sum -= abs(x) 
        if sum in dic.keys():
            cont += dic[sum]
    return cont

if __name__ == '__main__':
    a1 = [52297, 19954, 98865, 56832, 70365, 16992, 86920, 94792, 3054, 66344, 10270, 30949, 51221, 62978, 92740, 29614, 11290, 75621, 55322, 43420, 41171, 10470, 25412, 91689, 87030, 29511, 97243, 63682, 32926, 35245, 55914, 10444, 40350, 31252, 63807, 47096, 48478, 40617, 26798, 53995, 43201, 93228, 9367, 85876, 92286, 40034, 59646, 42377, 73193, 17502, 79856, 18123, 35625, 50198, 23619, 20556, 26857, 89246, 1482, 80282, 27068, 27068, 27068, 27068, 27068, 27068, 27068, 27068, 27068, 27068]
    t1 =  27068
    x1 = 0
    a = [11,5,3]
    t = 7
    x = 2
    print(count(a1, t1, x1)) # sol 8

'''
def count(a, t, x):
    return sum(not (t-v)%x if x else t==v for v in a)
'''
    