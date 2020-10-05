"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message. Ask the user for two numbers: one number to
    check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user.
    If not, print a different appropriate message.
"""


def run(user_number):
    """Print out an appropriate message depending the number is even or odd and multiple of 4."""
    if user_number % 2 == 0:
        if user_number % 4 == 0:
            num = int(input("Enter a check number: "))
            check = int(input("Enter a number to divide: "))
            if num % check == 0:
                return print(f"{num} divides evenly into {check}")
            else:
                return print(f"{num} NOT divides evenly into {check}")
        return print(f"{user_number} is even")
    else:
        return print(f"{user_number} is odd")


if __name__ == "__main__":
    number = int(input("Please enter a number: "))
    run(number)
