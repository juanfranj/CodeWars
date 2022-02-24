def get_middle(s):
    return s[(len(s)//2)] if len(s) % 2 else s[(len(s)//2) - 1: (len(s)//2) + 1]


if __name__ == '__main__':
    s = "of"
    print(get_middle(s))

'''
def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]
   
'''