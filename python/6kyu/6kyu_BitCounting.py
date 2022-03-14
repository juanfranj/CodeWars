def count_bits(n):
    return sum([int(i) for i in str(bin(n))[2:] if i == '1'])
if __name__ == '__main__':
    n = 10
    print(count_bits(n))

'''
def countBits(n):
    return bin(n).count("1")
'''