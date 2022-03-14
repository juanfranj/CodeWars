def last_digit(n1, n2):
    patron, nums = encontrar_patron(n1)
    sol = nums[n2 % patron -1]
    #print(nums, patron, 2 % patron, nums[n2 % patron -1])
    return int(sol) if n2 > 0 else 1
def encontrar_patron(a):
    fin = False
    patron = 1
    nums = []
    while not fin and patron < 10:
        last = str(a**patron)[-1] 
        if last in nums:
            fin = True
        else:
            nums.append(last)
            patron += 1   
    return patron - 1, nums


if __name__ == '__main__':
    a = 4
    b = 0
    print(last_digit(a, b))

'''
def last_digit(n1, n2):
    return pow( n1, n2, 10 )
'''