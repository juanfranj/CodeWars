from re import findall
def to_camel_case(text):
    rex = r"[A-Za-z\d]+"
    arr = findall(rex, text)
    sol = "".join([arr[i].capitalize()  if i>=1 else arr[i] for i in range(len(arr))])
    return sol

if __name__ == '__main__':
    s = 'the-stealth-warrior'
    print(to_camel_case(s))

'''
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
'''