def solution(number):
    sol = [i for i in range(1,number) if i%3 == 0 or i%5 == 0]
    return sum(sol)

if __name__ == '__main__':
    number = 20000
    n = solution(number)
    print(f"La solucion para el numero {number} es {n}")