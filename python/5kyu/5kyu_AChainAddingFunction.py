class add(int):
    def __call__(self, n):
        return add(self + n)

if __name__ == '__main__':
    n = 1
    print(add(1)(2))

'''
def add(n):
    return MyInt(n)
    
class MyInt(object):
    def __init__(self, n):
        self.value = n

    def __add__(self, n):
        return MyInt(self.value + n)
        
    def __sub__(self, n):
        return MyInt(self.value - n)
        
    def __call__(self, n):
        return MyInt(self.value + n)
        
    def __eq__(self, other):
        if isinstance(other, MyInt):
            return self.value == other.value
        else:
            return self.value == other
'''