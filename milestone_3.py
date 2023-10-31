import random

def my_random_choice(seq):
    if not seq:
        raise ValueError("Sequence cannot be empty.")
    return seq[random.randint(0, len(seq) - 1)]


word_list = ["grapes", "strawberries", "apples", "pears", "kiwis"]

word = my_random_choice(word_list)



def ask_for_input(word):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if check_guess(guess,word):
                break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


def check_guess(guess,word):
    if guess in word:
            print("You guessed", guess)
            print("Good guess! '{}' is in the word".format(guess))
            return True
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False
   
        
        
# Step 4: Call ask_for_input function to test the code
ask_for_input(word)

guess = input("Guess a letter: ").lower()
check_guess(guess,"word")
print(word)
