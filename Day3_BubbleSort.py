def BubbleSort(unsortedlist):
    lengthOfList = len(unsortedlist)
    for i in range(lengthOfList):
        for j in range(lengthOfList-1):
            if unsortedlist[j] > unsortedlist[j + 1]:
                temp = unsortedlist[j]
                unsortedlist[j] = unsortedlist[j + 1]
                unsortedlist[j + 1] = temp


def main():
    mylist = []
    elements = int(input("How many numbers you want in your list: "))
    for i in range(elements):
        n = int(input("Enter your Number: "))
        mylist.append(n)
    print("My Unsorted List: ", mylist)
    BubbleSort(mylist)
    print("Sorted List: ", mylist)


if __name__ == "__main__":
    main()
