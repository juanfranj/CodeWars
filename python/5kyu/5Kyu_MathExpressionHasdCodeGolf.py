def e(inp_str):
    sol = int(inp_str[0])
    nums = [i for i in inp_str[1:] if i not in ['+', '-', '*', '/']]
    signos = [i for i in inp_str[1:] if i in ['+', '-', '*', '/']]
    for num, sig in zip(nums,signos):    
        if sig == '+': sol += int(num)
        elif sig == '-': sol -= int(num)
        elif sig == '*': sol *= int(num)
        elif sig == '/': sol /= int(num)
    return sol
            
            



if __name__ == '__main__':
   s = "2*-3"
   print(e(s))