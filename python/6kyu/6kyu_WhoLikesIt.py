def likes(names):
    if len(names) == 0:
        res = "no one likes this"
    elif len(names) == 1:
        res = f"{names[0]} likes this"
    elif len(names) == 2:
        res = f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        res = f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        res = f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

    return res


if __name__ == '__main__':
    names = ['Alex', 'Jacob', 'Mark', 'Max']
    res =  likes(names)
    print(res)

'''
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
'''