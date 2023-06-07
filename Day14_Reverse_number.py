def reverse_num(num: int) -> str:
    result = ""
    while num > 0:
        x = num % 10
        result += str(x)
        num = num // 10
    return result


def main():
    num = int(input("Enter a number to reverse "))
    print(reverse_num(num))


if __name__ == "__main__":
    main()
