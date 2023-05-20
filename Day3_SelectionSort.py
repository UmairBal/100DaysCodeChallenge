def SelectionSort(mylist):
    numOfElements = len(mylist)
    for i in range(numOfElements):
        mini = i
        for j in range(i + 1, numOfElements):
            if mylist[j] < mylist[mini]:
                mini = j
        mylist[i], mylist[mini] = mylist[mini], mylist[i]

    return mylist


def main():
    mylist = []
    elements = int(input("How many numbers you want in your list: "))
    for i in range(elements):
        n = int(input("Enter your Number: "))
        mylist.append(n)
    print("My Unsorted List: ", mylist)
    SelectionSort(mylist)
    print(mylist)


if __name__ == "__main__":
    main()
