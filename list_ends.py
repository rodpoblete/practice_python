"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
the first and last elements of the given list. For practice, write this code inside a function. """


def run():
    """Take a list and make a new list of only the first and least elements of the givens list."""
    a = [5, 10, 15, 20, 25]
    new_list = [a[i] for i in (0, -1)]
    print(f"The original list are {str(a)}")
    print(f"First and least elements on the new list {new_list}")


if __name__ == "__main__":
    run()
