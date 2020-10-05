"""Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that
reads the same forwards and backwards.) """


def run(word_check):
    """Check the word is a palindrome or not."""
    clean_string = word_check.lower().replace(" ", "")
    if clean_string == clean_string[::-1]:
        return print(f"{word_check} is palindrome")
    else:
        return print(f"{word_check} is NOT a palindrome: {word_check[::-1]}")


if __name__ == "__main__":
    user_string = input("Please enter a sentence: ")
    run(user_string)
