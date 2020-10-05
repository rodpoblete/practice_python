"""Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below. """


def run():
    """Ask a user for a number and determine whether the number is prime or not."""
    user_number = int(input("Please enter a number: "))
    if user_number < 1:
        return print(f"{user_number} NOT a prime!")
    elif user_number == 2:
        return print(f"{user_number} IS prime!")
    else:
        for i in range(2, user_number):
            if user_number % i == 0:
                return print(f"{user_number} NOT a prime!")
        return print(f"{user_number} IS prime!")


if __name__ == "__main__":
    run()
