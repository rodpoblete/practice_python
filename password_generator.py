"""Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""
import random


def run(password):
    """Generate two types of passwords. Weak (only letters and 6 characters) or strong (full simbols and 8
    characters)."""
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = ["#", "$", "%", "&", "=", "*", "-", "+", "!", "(", ")", "/"]
    letters_upper = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "X",
        "W",
        "Y",
        "Z",
    ]
    letters_lower = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "x",
        "w",
        "y",
        "z",
    ]
    full_list_characters = numbers + symbols + letters_upper + letters_lower
    list_only_letters = letters_lower + letters_upper

    list_password = []

    if password == "weak":
        for i in range(6):
            character_random = random.choice(list_only_letters)
            list_password.append(character_random)

        final_password = "".join(list_password)

        return print(f"Your {password} 🦴 password is: {final_password}")
    elif password == "strong":
        for i in range(9):
            character_random = random.choice(full_list_characters)
            list_password.append(character_random)

        final_password = "".join(list_password)

        return print(f"Your {password} 💪 password is: {final_password}")
    else:
        return print(f"Please type only strong or weak 🤦‍♂️")


if __name__ == "__main__":
    option = input("How want your password (strong/weak) 🔐: ")
    run(option)
