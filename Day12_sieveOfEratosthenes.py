def prime_or_not(num):
    check = True
    for i in range(2, num-1):
        if num % i == 0:
            check = False

    return check


def primes_in_range(num):
    primes = []
    for i in range(2, num):
        check = prime_or_not(i)
        if check:
            primes.append(i)
    return primes


def main():
    num = int(input("Enter a number: "))
    primes = primes_in_range(num)
    print(primes)


if __name__ == "__main__":
    main()


