def factorofnum(a):
    factors = []
    for i in range(1, a+1):
        if a % i == 0:
            factors.append(i)
    return factors


def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter 2nd number: "))
    list1 = factorofnum(a)
    list2 = factorofnum(b)

    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)

    gcd = 0
    for i in common_elements:
        if i > gcd:
            gcd = i
    print("GCD of two numbers", a, b, "is", gcd)


if __name__ == "__main__":
    main()
