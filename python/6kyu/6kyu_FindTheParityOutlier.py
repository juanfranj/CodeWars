def find_outlier(integers):
    par = tipo_lista(integers[0:4])
    if par:
        for i in integers:
            if i%2 != 0:
                sol = i 
                break
    else:
        for i in integers:
            if i%2 == 0:
                sol = i
                break
    return sol

def tipo_lista(l):
    par = [i for i in l if i%2 == 0]
    return True if len(par) > 1 else False
    
    
if __name__ == '__main__':
    l = [2, 4, 0, 100, 4, 11, 2602, 36]
    print(find_outlier(l))

'''
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
'''