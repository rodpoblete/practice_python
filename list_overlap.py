"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without
duplicates). Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
import random


def run():
    """Return a list with de commons elements of other two random list."""
    a = []
    for i in range(10):
        a.append(random.randrange(1, 10, 1))
    b = []
    for i in range(17):
        b.append(random.randrange(1, 15, 2))
    c = []
    clean_list = []
    a.sort()
    b.sort()
    if len(a) > len(b):
        for element_a in a:
            for element_b in b:
                if element_a == element_b:
                    c.append(element_a)
    elif len(b) > len(a):
        for element_b in b:
            for element_a in a:
                if element_b == element_a:
                    c.append(element_b)

    for i in c:
        if i not in clean_list:
            clean_list.append(i)

    return print(
        f"List 1: {a}\nList2: {b}\nCommon elements are ({len(clean_list)}): {clean_list}"
    )


if __name__ == "__main__":
    run()
