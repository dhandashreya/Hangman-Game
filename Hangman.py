import time
import random
import urllib.request
show = ""
word = ""
choice = ""
length = 0
count = 0
actual_word = ""
already_guessed = []
all_guess = []
print("            HANGMAN GAME               ")
player_name = input("Enter your name:-")
print("Welcome to te game", player_name)
print("Let's play hangman!!!")


# function to choose a random word as hangman word
def main():
    global word
    global show
    global length
    global actual_word
    global already_guessed
    global all_guess
    already_guessed = []  # list that will have only correct guesses
    all_guess = []  # list that will have all guesses irrespective of right or wrong
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    guess_words_pile = long_txt.splitlines()
    word = random.choice(guess_words_pile)
    word = word.lower()  # word will be in lowercase only
    actual_word = word
    length = len(word)
    show = "*"*length  # all characters of word will be replaced by "*"


# function to ask user's choice to play game or not
def play():
    global choice
    global count  # count will show the number of wrong guess
    count = 0
    choice = input("Do you want to play the game again? If yes press y and for no press n:- ")
    print()
    choice_list = ["y", "Y", "n", "N"]
    while choice not in choice_list:
        print("Please enter the correct choice")
        choice = input("Do you want to play the game again? If yes press y and for no press n:- ")
        print()
    if choice == "y" or choice == "Y":
        main()
        hangman()
    elif choice == "n" or choice == "N":
        print("Thankyou for playing the game", player_name)
        print("X--------------GAME  OVER------------X")
        exit()


def hangman():
    limit = 5  # the number of acceptable wrong guesses
    global show
    global word
    global length
    global count
    global all_guess
    global already_guessed
    print("This is your Hangman word", show)
    print("Enter your guess")
    guess = input().strip()
    guess = guess.lower()  # guess will be converted in lowercase
    all_guess.append(guess)
    all_guess_count = all_guess.count(guess)              # number of times user's guess occurs in all_guess list
    word_count = word.count(guess)                        # number of times user's guess occurs in the word
    already_guessed_count = already_guessed.count(guess)  # number of times user's guess occurs in already_guessed list

    # only single letter is acceptable as guess either in uppercase or lowercase or else invalid input
    if len(guess) == 0 or len(guess) >= 2 or guess <= "9":
        print("Invalid input, try a letter")
        hangman()
    elif guess in word and already_guessed_count <= word_count:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index]+"*"+word[index+1:]
        show = show[:index]+guess+show[index+1:]
        print("Correct guess!!!")
        print()

    #  when a correct letter is guessed again
    elif guess in already_guessed and already_guessed_count > word_count:
        print("Already guessed,try guessing another letter")
        print()

    #  when a wrong letter is guessed again
    elif all_guess_count >= 2 and guess not in word:
        print("Wrong guess")
        print("You have already guessed it")

    # when a wrong letter is guessed for the first time
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess,", limit-count, "guesses remaining")
            print()
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess,", limit - count, "guesses remaining")
            print()
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess,", limit - count, "guesses remaining")
            print()
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess,", limit - count, "guesses remaining")
            print()
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess,, you are hanged!!!")
            print("The word was:", actual_word)
            print()
            play()

    if word == "*"*length:
        print("Congratulations!!!, you have guessed the word correctly")
        print("The word is", actual_word)
        play()
    elif count != limit:
        hangman()


if __name__ == "__main__":
    main()
    hangman()
