"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list
    in it and print out this new list. Write this in one line of Python. Ask the user for a number and return a list
    that contains only elements from the original list a that are smaller than that number given by the user.
"""


def run(check_number):
    """Print out all the elements of the list that are less than 5 and the different list list less user number input"""
    list_original = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_less_five = []
    list_less_user_number = []
    for element in list_original:
        if element < 5:
            list_less_five.append(element)
        if element < check_number:
            list_less_user_number.append(element)
    return print(
        f"Original list: {list_original}\nList less five: {list_less_five}\nList less user number ({check_number}): "
        f"{list_less_user_number}"
    )


if __name__ == "__main__":
    number = int(input("Enter a number to check the list: "))
    run(number)
