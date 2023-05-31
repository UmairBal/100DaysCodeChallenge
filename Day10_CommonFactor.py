def factors(number):
    factors_of_number = [1]
    for i in range(2, number // 2):
        if number % i == 0:
            factors_of_number.append(i)

    factors_of_number.append(number)
    return factors_of_number


def common_factor(x, y):
    factors_of_x = factors(x)
    factors_of_y = factors(y)
    common_factors = []
    for i in factors_of_x:
        for j in factors_of_y:
            if i == j:
                common_factors.append(i)
    return common_factors


def main():
    print(".............Program to Find common factor between two numbers........")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    common_factors = common_factor(x, y)
    print(common_factors)


if __name__ == "__main__":
    main()
