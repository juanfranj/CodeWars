from collections import Counter

def first_non_repeating_letter(string):
    dic = Counter(string.lower())
    print(dic)
    sol = ''
    for key in dic.keys():
        if dic[key] == 1:
            sol = key
            break
    return sol if sol in string else sol.upper()

if __name__ == '__main__':
    s = 'sTreSS'
    print(first_non_repeating_letter(s))
