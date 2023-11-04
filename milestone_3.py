import random


word_list = ["grapes", "strawberries", "apples", "pears", "kiwis"]

word = random.choice(word_list)


def ask_for_input():
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    return guess

def check_guess(word, guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

user_input = ask_for_input()

check_guess(word, user_input)
