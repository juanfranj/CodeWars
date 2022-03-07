from collections import Counter

def scramble(s1, s2):
    dic_1 = Counter(s1)
    dic_2 = Counter(s2)
    sol = True
    for key in dic_2.keys():
        #print(key, dic_1.keys(), dic_1.get(key))
        if key not in dic_1.keys():
            sol = False
            break
        else:
            if dic_2[key] > dic_1[key]:
                sol = False
                break
    return sol


if __name__ == '__main__':
    s1 = 'rkqodlw' 
    s2 = 'world'
    sol = scramble(s1, s2)
    print(sol)
'''
def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True
'''