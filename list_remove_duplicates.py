"""Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
list minus all the duplicates.

Extras:

    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function."""
import random


def method_loop():
    """Take a list and return a new list that contains all the elements of the first
    list minus all the duplicates using list comprehensions."""
    a = []
    for i in range(10):
        a.append(random.randrange(1, 10, 1))

    loop_list = []
    [loop_list.append(x) for x in a if x not in loop_list]
    loop_list.sort()

    print(f"Original list {str(a)}")
    print(f"The list after removing duplicates: {str(loop_list)}")


def method_set():
    """Take a list and return a new list that contains all the elements of the first
    list minus all the duplicates using set built-in function."""
    b = []
    for i in range(10):
        b.append(random.randrange(1, 10, 1))

    clean_list = list(set(b))

    print(f"Original list {str(b)}")
    print(f"The list after removing duplicates: {str(clean_list)}")


if __name__ == "__main__":
    method_loop()
    method_set()
