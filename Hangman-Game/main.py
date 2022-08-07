import random
import time

print("WELCOME TO HANGMAN GAME")
print("-----------------------")
name = input("Enter your name: ")
print(f"Welcome, {name}. Best of luck!")
time.sleep(1)
print(f"Don't forget {name}, sometimes words have the same letter several times!!")
time.sleep(2)
print("----------------")
print("The game starts!")
print("----------------")
time.sleep(2)


def main_of_the_game():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["computer", "programming", "electronics", "mouse", "temperature", "robot", "phone", "smart",
                      "motor", "facebook", "machine", "sadness", "television", "coffee", "button", "curtain", "plane",
                      "light", "electric", "copper", "silver", "bottle", "picture", "lotion", "shampoo", "chain",
                      "religion", "chair", "jacket", "radio", "cable", "internet", "bicycle", "money"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_" * length
    already_guessed = []
    play_game = ""


def playing_loop():
    global play_game
    play_game = input(f"Do you want to play again {name} (Y/N)? ")
    play_game = play_game.lower()
    while play_game not in ["y", "yes", "no", "n"]:
        play_game = input(f"Do you want to play again {name} (Y/N)? ")
    if play_game == "yes" or "y":
        main_of_the_game()
    elif play_game == "no" or "n":
        print(f"Thanks for playing! I hope you enjoyed it {name}")
        time.sleep(2)
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5

    guess = input("This is the Hangman word: " + display + " Enter your guess: \n")
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print(f"Invalid input {name}, try a letter.\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print(f"You already guessed this letter {name}, Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__")
            print("Wrong guess. " + str(limit - count) + "guesses remaining.\n")

        elif count == 2:
            time.sleep(1)
            print("  _____\n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__")
            print("Wrong guess. " + str(limit - count) + "guesses remaining.\n")

        elif count == 3:
            time.sleep(1)
            print("  _____\n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__")
            print("Wrong guess. " + str(limit - count) + "guesses remaining.\n")

        elif count == 4:
            time.sleep(1)
            print("  _____\n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |      \n"
                  "  |      \n"
                  "__|__")
            print("Wrong guess. " + str(limit - count) + "last guess remaining.\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__")
            print(f"Wrong guess. You are hanged, {name}!\n")
            print("The word was: ", already_guessed, word)
            playing_loop()

    if word == '_' * length:
        print(f"Congrats {name}! You guessed correctly!")
        playing_loop()
    elif count != limit:
        hangman()


main_of_the_game()

hangman()
