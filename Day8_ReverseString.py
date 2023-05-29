def reverse_string(string):
    i = len(string)-1
    while i >= 0:
        print(string[i], end="")
        i -= 1


def main():
    string = input("Enter the string you want to convert: ")
    reverse_string(string)


if __name__ == "__main__":
    main()
