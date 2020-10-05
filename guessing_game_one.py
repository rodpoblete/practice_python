"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very
first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out."""
import random


def run():
    """Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
    whether they guessed too low, too high, or exactly right."""
    random_number = random.randint(1, 9)
    counter = 0

    while True:
        user_input = int(input("Please enter a number to guess (1 - 9): "))
        if user_input < random_number:
            print("Too slow 👇")
            option = input(
                "You can type 'exit' to close the game or enter to keep going: "
            )
            counter += 1
            if option == "":
                continue
            elif option == "exit":
                break
        elif user_input > random_number:
            print("Too high 👆")
            counter += 1
            option = input(
                "You can type 'exit' to close the game or enter to keep going: "
            )
            if option == "":
                continue
            elif option == "exit":
                break
        elif user_input == random_number:
            print("Exactly right 👏")
            counter += 1
            break

    print(f"You guess the number in {counter} attempts 🏁")


if __name__ == "__main__":
    run()
