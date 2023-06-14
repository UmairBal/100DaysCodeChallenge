def palindrome(text: str):
    palin = []
    for i in reversed(range(len(text))):
        palin.append(text[i])
    string = ''.join(palin)
    if text == string:
        return True
    else:
        return False


def substrings(string: str):
    substring = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring.append(string[i:j])
    return substring


def longest_palindrome(substring: list):
    new_sub_string = [word for word in substring if palindrome(word)]
    new_sub_string.sort(key=len, reverse=True)
    if new_sub_string:
        print("palindrome is: ", new_sub_string[0])
    else:
        print("no palindrome found")



def main():
    text = input("Enter your text: ")
    substring = substrings(text)
    longest_palindrome(substring)


if __name__ == "__main__":
    main()
