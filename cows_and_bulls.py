""" Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a
“bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the
correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the
user at the end. """
import random


def run(user_number):
    random_number = random.randint(1000, 2000)
    list_random_number = [int(x) for x in str(random_number)]
    list_user_number = [int(y) for y in str(user_number)]
    cow = 0
    bull = 0

    for i in range(len(list_random_number)):
        if list_random_number[i] == list_user_number[i]:
            cow += 1
        elif list_user_number[i] in list_random_number:
            bull += 1

    print(f"random generate number: {random_number}")
    print(f"{cow} 🐄, {bull} 🐂")


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    run(number)
