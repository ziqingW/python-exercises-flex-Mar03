width = int(input("Width? "))
height = int(input("Height? "))
print("*" * width)
for i in range(height - 2):
    print("*{}*".format(" "*(width - 2)))
print("*" * width)