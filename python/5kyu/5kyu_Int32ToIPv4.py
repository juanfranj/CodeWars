def int32_to_ip(int32):
    #num = "{:032b}".format(int32)
    num = f"{int32:032b}"
    arr = [num[i:i+8] for i in range(0,25,8)]
    sol = ".".join([str(int(i, 2)) for i in arr])
    return sol


if __name__ == '__main__':
    n = 236598754
    print(int32_to_ip(n))

'''
from ipaddress import IPv4Address

def int32_to_ip(int32):
    return str(IPv4Address(int32))

def int32_to_ip(int32):
    return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))

'''