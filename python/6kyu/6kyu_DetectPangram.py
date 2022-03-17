import string
def is_pangram(s):
    dic = {k:v for k, v in zip(string.ascii_lowercase, [0 for i in range(27)])}
    for i in s.lower():
       if i in dic.keys():
           dic[i] += 1
    return False if 0 in dic.values() else True


    return False
if __name__ == '__main__':
    #print(string.ascii_lowercase)
    pangram = "The quick, brown fox jumps over the lazy dog!"
    print(is_pangram(pangram))
'''
import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
'''