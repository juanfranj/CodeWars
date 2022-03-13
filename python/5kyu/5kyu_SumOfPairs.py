def sum_pairs(nums, sum_value):
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            return [diff, num]
        seen.add(num)

if __name__ == '__main__':
    l1 =  [10, 5, 2, 3, 7, 5]
    print(sum_pairs(l1, 10))
    
