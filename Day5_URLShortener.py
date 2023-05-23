import random
import string


# To generate the random code
def generate_random_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(6))
    return code


# URL Shortening code

def url_shortner(original_url):
    short_url = ""
    database = {}
    while True:
        code = generate_random_code()
        if code not in database:
            break

    database[code] = original_url

    dot_found = False
    for char in original_url:
        if dot_found:
            if char == "/":
                break
            short_url += char

        elif char == ".":
            dot_found = True
            short_url += char

        else:
            short_url += char

    print(short_url)

def main():
    url = input("Enter the url you want to shorten: ")
    url_shortner(url)


if __name__ == "__main__":
    main()
