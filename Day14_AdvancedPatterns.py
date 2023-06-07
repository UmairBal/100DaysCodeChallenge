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
