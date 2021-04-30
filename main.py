# Libraries used
import random
import time

# Variables
count = 0
display = ""
word = ""
already_guessed = []
play_again = ""

# Displaying the Username and Instructions to play the game
print("\n-----------------Welcome to Hangman game--------------------\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("\nInstructions:")
print("1.You have to guess the word of a particular category given.")
print("2.You will have six lives. For each incorrect guess, it will lead to the loss of one life.")
time.sleep(5)
input("\nPress Enter to START!")
print("\nThe game is about to start!")
print("Let's play Hangman!")
time.sleep(3)


# Drawing the Pattern depending upon the incorrect answers
def draw_man(progress):
    #    _____
    #   |     |
    #   |     |
    #   |     |
    #   |     O
    #   |    /|\
    #   |    / \
    # __|__

    if progress == 1:
        time.sleep(1)
        print("         \n" +
              "  |      \n" +
              "  |      \n" +
              "  |      \n" +
              "  |      \n" +
              "  |      \n" +
              "  |      \n" +
              "__|__\n")

    if progress == 2:
        time.sleep(1)
        print("   _____ \n" +
              "  |      \n" +
              "  |      \n" +
              "  |      \n" +
              "  |      \n" +
              "  |      \n" +
              "  |      \n" +
              "__|__\n")

    elif progress == 3:
        time.sleep(1)
        print("   _____ \n" +
              "  |     | \n" +
              "  |     |\n" +
              "  |      \n" +
              "  |      \n" +
              "  |      \n" +
              "  |      \n" +
              "__|__\n")

    elif progress == 4:
        time.sleep(1)
        print("   _____ \n" +
              "  |     | \n" +
              "  |     |\n" +
              "  |     | \n" +
              "  |      \n" +
              "  |      \n" +
              "  |      \n" +
              "__|__\n")

    elif progress == 5:
        time.sleep(1)
        print("   _____ \n" +
              "  |     | \n" +
              "  |     |\n" +
              "  |     | \n" +
              "  |     O \n" +
              "  |      \n" +
              "  |      \n" +
              "__|__\n")

    elif progress == 6:
        time.sleep(1)
        print("   _____ \n" +
              "  |     | \n" +
              "  |     |\n" +
              "  |     | \n" +
              "  |     O \n" +
              "  |    /|\ \n" +
              "  |    / \ \n" +
              "__|__\n")
    return


# Main Function where initialization and random word chosen to be guessed
def main():
    global count
    global display
    global word
    global already_guessed
    global play_again

    # Word stored depending upon their types
    category = {"Color": ["green", "pink", "lemon", "orange", "violet", "yellow", "indigo", "blue", "purple"],
                "Language": ["Python", "Spanish", "Java", "English", "HTML", "Chinese", "Telugu", "Indonesian"],
                "Animal": ["tiger", "lion", "jackal", "elephant", "kangaroo", "snake"]}
    category_choice = random.choice(list(category.keys()))

    # Printing the category of word to be guessed
    print("\nCategory of the word you need to guess: " + category_choice)
    word = random.choice(category[category_choice])
    count = 0
    display = '_' * len(word)
    already_guessed = []
    play_again = ""
    hangman()


# Asking user to play again or leave the game
def play_loop():
    global play_again
    play_again = input("\nWant to play Again? Press y or Y for YES and n or N for NO :")
    while play_again in ["y", "Y"]:
        main()
        play_again = input("Want to play Again? Press y or Y for YES and n or N for NO :")
    else:
        print("Thanks For Playing! We expect you back again!")
        exit()


# Hangman Function Used to check correctness of guessed letter
def hangman():
    word_progress = ["-"] * len(word)

    # It is used to keep track of all letter guessed
    guessed = []

    # user can only have 6 incorrect guesses
    incorrect = 0

    # main Operation for hangman Game Starts here
    while incorrect < 6 and "-" in word_progress:
        print()
        # draw_man function used to display the DESIGN

        print(" ".join(word_progress))
        if len(guessed) != 0:
            print("\nGuessed letters: ")
            print(" ".join(guessed))
        print()

        # Here user is asked to enter for alphabetical guess, which will be forced  to lowercase
        guess = "0"
        if not guess.isalpha():
            guess = input("Guess a letter or the word: ").lower()

        if guess == word.lower():
            # Completely guessed the right word (Its time for reward)
            break

        # You Have entered word instead of letter
        elif len(guess) > 1:
            print("Sorry, that's not the letter. You have entered a word ")
            incorrect += 1
            draw_man(incorrect)

        # You have already guessed the letter
        elif guess in guessed:
            print("You have already guessed that letter.")

        # Incorrect Guess
        elif guess not in word.lower():
            print(guess + " is not in the word.")
            incorrect += 1
            guessed.append(guess)
            draw_man(incorrect)

        # Correctly guessed the letter which is present in the word
        else:
            print(guess + " is in the word!")
            guessed.append(guess)

            # Replacing the - withe the correct letter that user have guessed
            for i in range(len(word)):
                if word_progress[i] == "-" and word[i].lower() == guess:
                    word_progress[i] = word[i]  # to make original caps show up

        print("*********************************************************************************************")
    print()
    if incorrect == 6:
        draw_man(incorrect)
        print("You lost!")
        print("\nThe word was: " + word)
    else:  # we're out of the loop because we found or guessed the word
        print("\nYou found the word! You win!")

    # either way, show their final progress
    print(" ".join(word))
    print("Guessed letters: ")
    print(" ".join(guessed))
    play_loop()


if __name__ == "__main__":
    main()
