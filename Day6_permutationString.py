import itertools


def permutation_of_number(string, password):
    check = False
    combinations = itertools.permutations(string)
    for combination in combinations:

        combination = ''.join(combination)
        if combination == password:
            print("Password Found")
            check = True

    if check == False:
        print("Password Not Found!")


def main():
    password = "new"
    string = input("Enter your string: ")
    permutation_of_number(string, password)


if __name__ == "__main__":
    main()
