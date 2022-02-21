def high_and_low(numbers):
    min = "1000"
    max = "-1000"
    for i in numbers.split(" "):
        
        if int(i) < int(min):
            min = i
        if int(i) > int(max):
            max = i

    return max + " " + min

if __name__ == '__main__':
    st = "10 2 -2 -10"
    print(high_and_low(st))
    #print(int(-1E15))

'''
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))

'''