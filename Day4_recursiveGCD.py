def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(gcd(a, b))


if __name__ == "__main__":
    main()
