"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock"""


def run():
    """Compare input two players, compare and print out the message to the winner."""
    while True:
        player1 = input("(Player 1) Enter rock-paper-scissors: ")
        player2 = input("(Player 2) Enter rock-paper-scissors: ")

        if (
            (player1 == "rock" and player2 == "scissors")
            or (player1 == "scissors" and player2 == "paper")
            or (player1 == "paper" and player2 == "rock")
        ):
            print("Congrats Player 1 wins!")
            option = input("Start a new game? (y/n): ")
            if option == "n":
                break
        elif (
            (player2 == "rock" and player1 == "scissors")
            or (player2 == "scissors" and player1 == "paper")
            or (player2 == "paper" and player1 == "rock")
        ):
            print("Congrats Player 2 wins!")
            option = input("Start a new game? (y/n): ")
            if option == "n":
                break
        elif player1 == player2:
            print("Draw...")
            option = input("Start a new game? (y/n): ")
            if option == "n":
                break


if __name__ == "__main__":
    run()
