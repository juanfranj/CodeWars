def make_readable(seconds):

    min = seconds // 60
    seg = seconds % 60
    h   = min // 60
    min = min % 60

    return f"{h:02d}:{min:02d}:{seg:02d}"

if __name__ == '__main__':
    seconds = 00
    t = make_readable(seconds)
    print(t)
'''
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
'''
