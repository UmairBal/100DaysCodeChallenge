##################### Star Pattern ######################

n = int(input("Enter a number "))
for i in range(1, n):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()

for i in range(1, n):
    for j in range(i):
        print(" ", end="")
    for k in range(1, n - i + 1):
        print("* ", end="")
    print()

##################### Zig Zag Pattern #####################

for i in range(1, 4):
    for j in range(1, n+1):
        if (((i+j) % 4) == 0) or (i == 2 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()

