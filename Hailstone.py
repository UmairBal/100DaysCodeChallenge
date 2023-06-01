def hailstone_sequence(number):
    print(number,end="->")
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number, end="->")
        else:
            number = (number * 3) + 1
            print(number, end="->")


def main():
    number = int(input("Enter your number: "))
    hailstone_sequence(number)


if __name__ == "__main__":
    main()
