def find_short(s):
    s=s.split(" ")
    l=100
    for i in range(len(s)):
        if len(s[i])<l:
            l=len(s[i])
    return l 