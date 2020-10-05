"""Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the
    previous message. (Hint: order of operations exists in Python) Print out that many copies of the previous message
    on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
import datetime


def run(name_user, age_user, numbers_of_copies):
    """Print a message tells a user the year the will turn 100 years old and the numbers of copies."""
    now = datetime.datetime.now()
    actual_year = now.year
    difference = 100 - age
    hundred_year = actual_year + difference
    print(
        f"{name_user} you have {age_user} and the year that will turn 100 years old is {hundred_year}\n"
        * numbers_of_copies
    )


if __name__ == "__main__":
    name = input("Please enter your name: ")
    age = int(input("Please enter a age (be honest 🤭): "))
    copies = int(input("How many copies of the message yo have?: "))
    run(name, age, copies)
