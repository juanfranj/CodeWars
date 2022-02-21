def find_it(seq):
    dic = {}
    for key in seq:
        if key not in dic.keys():
            dic[key] = 1
        else:
            dic[key] += 1
    for key in dic.keys():
        if dic[key]%2 != 0:
            return key

if __name__ == '__main__':
    sec = [1,1,2,-2,5,2,4,4,-1,-2,5]
    sol = find_it(sec)
    print(sol)

'''
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
'''