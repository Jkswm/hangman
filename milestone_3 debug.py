import random

def my_random_choice(seq):
    if not seq:
        raise ValueError("Sequence cannot be empty.")
    return seq[random.randint(0, len(seq) - 1)]


word_list = ["grapes", "strawberries", "apples", "pears", "kiwis"]

word = my_random_choice(word_list)

   
def ask_for_input(word):
    guess = input("Guess a letter: ").lower()
    while True:
        if len(guess) == 1 and guess.isalpha():
            if check_guess(guess):
                break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


def check_guess(guess, word):
    if guess in word:
        print("You guessed", guess)
        print("Good guess!")
        return True
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False

guess = input("Guess a letter: ").lower()
ask_for_input(word)
check_guess(guess,word)