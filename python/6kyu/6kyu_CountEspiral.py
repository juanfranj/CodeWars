def spiral_sum(size):
    
    return size**2//2 + size if size % 2 else size**2//2 + (size - 1)

def espiral(size):
    for i in range(3,size+1):
        num = spiral_sum(i)
        if i % 100 == 0:
            print(num)

if __name__ == '__main__':
    size = 1000
    espiral(size)