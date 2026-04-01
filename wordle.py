# Assessment Task 3 (AT3): Project
#
# Author: Pallavi Kulkarni
# Student ID: 20153679
#
# Course: Certificate IV in IT (Programming)
# Lecturer: Mr Rafael Avigad

""" This program contains the functions to play the clone of wordle game.Example, play_game, test_game score_guess, read_words_from_file, random_target_word and display_score"""

from random import choice

# Variables and Constants
DEBUG = False
target_word_filename = "target_words.txt"
all_word_filename = "all_words.txt"

# Application Functions

def score_guess(guess, target):
    """Calculates the score of a guess against the target.

    Parameters
    ----------
    guess: The word entered by the user as a guess.
    target: The word of day chosen randomly from target file

    Returns
    -------
    list score calculated by the guess against the target.
    0 if the letter at position in guess is not in target
    1 if the letter at position in guess is in target but not in same position
    2 if the letter at position in guess is in the same position

    Examples
    ---------
    >>> score = score_guess('hello', 'train')
    >>> print(score)
    [0, 0, 0, 0, 0]


    >>> score = score_guess('world', 'train')
    >>> print(score)
    [0, 0, 1, 0, 0]

    >>> score = score_guess('hello', 'hello')
    >>> print(score)
    [2, 2, 2, 2, 2]
    """
    length = len(target)
    calculated_score = [0] * length
    if guess == target:
        calculated_score = [2, 2, 2, 2, 2]
    else:
        for position in range(length):
            if guess[position] == target[position]:
                calculated_score[position] = 2
            elif guess[position] in target:
                calculated_score[position] = 1
            else:
                calculated_score[position] = 0
            position += 1

    return calculated_score


def read_words_from_file(filename):
    """Reads words from a file and returns them as a list.
     Parameters
    ----------
    filename: The name of the file to be read

    Returns
    -------
    The list of words from file

    Examples
    ---------
    >>> word_list = read_words_from_file( "target_words.txt")
    >>> print(word_list[:3])
    ['aback', 'abase', 'abate']

    """
    words = []
    with open(filename, 'r') as file:
        while  True:
            word = file.readline().strip()
            if not word:
                break
            words.append(word)
    return words


def show_greeting(name):
    print("Welcome " + name + "!")


def show_instructions():
    print("****Instructions****")
    print("You get six chances to guess a five letter target. ")
    print("Don't worry! You will get clues")
    print("Against each letter in the guessed word, you see symbols")
    print("X : The letter is at the right place in target")
    print("? : The letter is in the target, but at different position")
    print("- : The letter is not present in the target word\n")


def random_target_word(word_list):
    """Randomly chooses a word from a list of words."""
    # number_of_words = len(word_list)
    random_word = choice(word_list)
    return random_word

def display_score(new_score, guess):
    """Displays the score of a guess against the target."""
    score_output = ""
    word_output = ""

    for score_index in range(len(new_score)):
        if new_score[score_index] == 0:
            score_output += "- "
        elif new_score[score_index] == 1:
            score_output += "? "
        elif new_score[score_index] == 2:
            score_output += "X "

    for guess_index in range(len(guess)):
        word_output += guess[guess_index]
        word_output += " "

    print(score_output)
    print(word_output)

def play_game():
    print("Let's Play The Game!")
    name = input("Please enter your name: ")
    if name == "":
      name = "Random user"
    show_greeting(name)
    while True:
        choice = input("Would you like to read instructions Y/N?")
        choice = choice.upper()
        if choice == "Y":
            show_instructions()
            break
        elif choice == "N":
            break
        else:
            print("Please enter right choice!")
            continue

    target_word_list = read_words_from_file(target_word_filename)
    all_word_list = read_words_from_file(all_word_filename)
    word = random_target_word(target_word_list)
    print(word)
    guesses = 6
    status = "Unsuccessful"
    while guesses > 0:
        guess = input("Guess a five letter word: ")
        guess = guess.lower()
        guesses -= 1
        if len(guess) < 5:
            print("The word is too short")
        elif len(guess) > 5:
            print("The word is too long")
        elif guess not in all_word_list:
            print("Sorry, that's not a valid word.")
        else:
            score = score_guess(guess, word)
            display_score(score, guess)
            contains_only_twos = all(item == 2 for item in score)
            if contains_only_twos:
                print("Congratulations! You guessed it!")
                status = "successful"
                break
            else:
                print("You have " + str(guesses) + " guesses left.")
        if guesses == 0:
            print("Oh.. you are out of guesses...\nBetter luck next time!")
            print("The Word was " + word)

    with open('play_list.txt', 'a') as file:
        record = f"{name} {status} {6-guesses} {word} \n"
        file.writelines(record)


def test_game():
    """ Tests the game """
    # Test Case 1
    ## Arrange
    guess_word = "hello"
    target_word = "train"

    ## Act
    score = score_guess(guess_word, target_word)

    ## Assert
    print("Score:", score, "Expected:", [0, 0, 0, 0, 0])


    # Test Case 2
    ## Arrange
    guess_word = "hello"
    target_word = "hello"

    ## Act
    score = score_guess(guess_word, target_word)

    ## Assert
    print("Score:", score, "Expected:", [2, 2, 2, 2, 2])


    # Test Case 3
    ## Arrange
    guess_word = "world"
    target_word = "hello"

    ##Act
    score = score_guess(guess_word, target_word)

    ## Assert
    print("Score:", score, "Expected:", [0, 1, 0, 2, 0])


    # Test Case 4

    ## Act
    all_word_list = read_words_from_file(all_word_filename)

    ## Assert
    print("Got:", all_word_list[:5], "Expected:", ['aahed', 'aalii', 'aargh', 'aarti', 'abaca'])


    # Test Case 5

    ## Act
    target_word_list = read_words_from_file(target_word_filename)

    ## Assert
    print("Got:", target_word_list[-5:], "Expected:", ['young', 'youth', 'zebra', 'zesty', 'zonal'])


    # Test Case 6

    list_of_words = ["apple", "banana", "cherry"]

    for count in range(5):
        selected_word = random_target_word(list_of_words)
        print("Selected:", selected_word)


if DEBUG:
    test_game()
else:
    play_game()

