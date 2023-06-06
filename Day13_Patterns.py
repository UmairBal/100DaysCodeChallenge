################# Inverted Pattern ##################

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(1, n+1-i):
        print(j, end=" ")
    print()

################## 0-1 Pattern #####################

for i in range(1, n + 1):
    for j in range(i):
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
    
################## Rhombus pattern  #####################

for i in range(n):
    for j in range(1,n+1-i):
        print(" ", end=" ")
    for j in range(n):
        print("*", end=" ")
    print()




