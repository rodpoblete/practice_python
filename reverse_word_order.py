"""Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to
the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My}

shown back to me."""


def run(words):
    """Ask the user for long string containing multiple words and print back the user in backwards order."""
    split_words = words.split(" ")
    reversed_words = [word for word in reversed(split_words)]
    sentence = " ".join([str(word) for word in reversed_words])
    return print(sentence)


if __name__ == "__main__":
    user_string = input("Enter a words: ")
    run(user_string)
