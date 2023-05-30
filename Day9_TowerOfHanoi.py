def tower_of_hanoi(n, S, D, A):
    if n == 1:
        print("Move disk 1 from ", S, "to", D)
        return
    tower_of_hanoi(n - 1, S, A, D)
    print("Move disk", n, "from", S, "to", D)
    tower_of_hanoi(n - 1, A, D, S)


def main():
    n = int(input("Enter the number of disks: "))
    source = "S"
    destination = "D"
    aux = "AUX"
    tower_of_hanoi(n, source, destination, aux)
    print("The number of steps that it take to complete is ", (2 ** n) - 1)


if __name__ == "__main__":
    main()
