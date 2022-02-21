def disemvowel(string_):
    return "".join([i for i in string_ if i not in 'aeiouAEIOU'])

if __name__ == '__main__':
    text = "*Unb ea^Iih#evXeECEOj Er(hI/Oc<oCXeE ?}*rNM]maEyxi=f"
    print(disemvowel(text))
    
'''
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
'''