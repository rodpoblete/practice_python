"""Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of
Python that takes this list a and makes a new list that has only the even elements of this list in it."""


def run():
    """Take a list a return a new one with only elements of the original."""
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [i for i in a if i % 2 == 0]
    return print(b)


if __name__ == "__main__":
    run()
