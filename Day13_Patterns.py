n = int(input("Enter a number: "))
for i in range(n):
    for j in range(1, n+1-i):
        print(j, end=" ")
    print()

