from itertools import permutations


def next_bigger(n):
    
    n = str(n)
    if len(n) < 10:
        text = tuple(list(str(n)))
        arr = sorted(set(permutations(n)))
        arr1 = [int("".join(i)) for i in arr]
        if arr.index(text) != len(arr)-1:
            sol = arr[arr.index(text)+1]
        else:
            sol = "-1"

        return int("".join(sol))

    else:
        
        n1 = n[:-6]
        n = n[-6:]
        text = tuple(list(str(n)))
        arr = sorted(set(permutations(n)))
        if arr.index(text) != len(arr)-1:
            sol = arr[arr.index(text)+1]
            return int(n1 + "".join(sol))
        else:
            return -1


if __name__ == '__main__':
    n = 1016297195310865
    print(next_bigger_(n))

    '''
    def next_bigger(n):
    nums = list(str(n))
    for i in reversed(range(len(nums[:-1]))):
        for j in reversed(range(i, len(nums))):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = sorted(nums[i + 1:])
                return int(''.join(nums))
    return -1
    '''