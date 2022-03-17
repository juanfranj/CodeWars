def solution(s):
    if len(s)%2 != 0:
        s += '_'
    return [s[i:(i+2)] for i in range(0,len(s),2)]

if __name__ == '__main__':
    s = "x"
    print(solution(s))

'''
def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
'''