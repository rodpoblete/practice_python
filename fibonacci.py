"""Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this
opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the
sequence to generate.(Hint: The Fibonnaci sequence is a sequence of numbers where the next number in the sequence is
the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …) """


def run():
    """Asks the user how many Fibonnaci numbers to generate and then generates them."""
    number = int(input("Please enter a number: "))
    a = 0
    b = 1
    if number <= 0:
        print("Incorrect sequence")
    elif number == 1:
        return b
    else:
        for i in range(2, number + 1):
            c = a + b
            a = b
            b = c
        return print(b)


if __name__ == "__main__":
    run()
