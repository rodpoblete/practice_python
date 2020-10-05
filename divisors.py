"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (
If you don’t know what a divisor is, it is a number that divides evenly into another number. For example,
13 is a divisor of 26 because 26 / 13 has no remainder.) """


def run(user_number):
    """Print out a list of all the divisors of a number. (Without remainder)"""
    list_numbers = []
    for element in range(1, user_number):
        if user_number % element == 0:
            list_numbers.append(element)
    return print(f"All divisors for {user_number} are {list_numbers}")


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    run(number)
