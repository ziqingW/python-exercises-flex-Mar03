height = int(input("What is the height? "))
for i in range(height):
    print("{space}{star}{space}".format(star = "*" * (i * 2 + 1), space = " " *(height - i)))