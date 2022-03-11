from re import findall
def alphanumeric(password):
    reg = r"^[a-zA-Z\d]+$"
    return True if len(findall(reg, password)) >= 1 else False
if __name__ == '__main__':
    s = 'PassW0rd'
    print(alphanumeric(s))

'''
def alphanumeric(string):
    return string.isalnum()
'''