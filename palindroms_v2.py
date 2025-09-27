def check_palindrome(candidate: str) -> bool:
    return candidate == candidate[::-1]

def check_palindrome_insensitive(candidate: str) -> bool:
    return candidate.upper() == candidate[::-1].upper()

def check_palindrome_text_only(candidate: str) -> bool:
    text_only = ''.join(znak for znak in candidate if znak.isalpha())
    return check_palindrome_insensitive(text_only)


def main():
    with open('symbole.txt', 'r') as file:
        symbols = [line.strip() for line in file]

    with open('symbole_result.txt', 'w') as file:
        for symbol in symbols:
            if check_palindrome(symbol):
                print(f"{symbol} palindrom")
                print(symbol, file=file)

if __name__ == "__main__":
    #main()
    print(check_palindrome_insensitive('KAjak'))
    print(check_palindrome_text_only('KA4324^&jak'))
