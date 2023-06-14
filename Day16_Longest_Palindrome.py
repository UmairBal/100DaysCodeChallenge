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
    max_val = 0
    point = 0
    longest_palindromes = []
    for i in substring:
        if palindrome(i):
            longest_palindromes.append(i)
    for i in range(len(longest_palindromes)):
        if len(longest_palindromes[i]) > max_val:
            max_val = len(longest_palindromes[i])
            point = i
    print("Longest Palindrome is: ", longest_palindromes[point])


def main():
    text = input("Enter your text: ")
    substring = substrings(text)
    longest_palindrome(substring)


if __name__ == "__main__":
    main()
