from itertools import combinations

def choose_best_sum(t, k, ls):
    suma = [sum(dis) for dis in list(combinations(ls, k)) if sum(dis) <= t]
    return max(suma) if len(suma) > 0 else None

if __name__ == '__main__':
    ls = [50, 55, 57, 58, 60]
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
    t = 430
    k = 8
    print(choose_best_sum(t, k, xs))
    '''
    import itertools
def choose_best_sum(t, k, ls):
    try: 
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None

from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)
    
    '''