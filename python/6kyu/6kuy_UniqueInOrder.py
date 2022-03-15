
def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    sol = [iterable[0]]
    for i in iterable[1:]:
        if i != sol[-1] :
            sol.append(i)
    return sol



if __name__ == '__main__':
    s = 'AAAABBBBCCCCcDDDDQQQQQAAAABBCD'
    print(unique_in_order(s))
    

'''
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]


'''