number = int(input("Give a number to start: "))
factors = [n for n in range(1, int(round(number/2)) + 1) if number % n == 0]
for num in set(factors):
    print(num)
    