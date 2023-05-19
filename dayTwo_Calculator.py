def choiceContinue():
    while True:
        choice = input("Do you want an other calculation (y/n): ")
        if choice == "y" or choice == "Y":
            return choice
        elif choice == "N" or choice == "n":
            return choice
        else:
            print("choice invalid!")
            continue


def main():
    while True:
        print("Enter your expression ")
        firstNumber = int(input("First Number: "))
        operation = input("Operator: ")
        secondNumber = int(input("Second Number: "))

        if operation == "*":
            result = firstNumber * secondNumber
            print(result)
            n = choiceContinue()
            if n == "y":
                continue
            else:
                break
        elif operation == "-":
            result = firstNumber - secondNumber
            print(result)
            n = choiceContinue()
            if n == "y":
                continue
            else:
                break
        elif operation == "+":
            result = firstNumber + secondNumber
            print(result)
            n = choiceContinue()
            if n == "y":
                continue
            else:
                break
        elif operation == "/":
            result = firstNumber / secondNumber
            print(result)
            n = choiceContinue()
            if n == "y":
                continue
            else:
                break
        else:
            print("invalid!")
            continue


if __name__ == "__main__":
    main()
