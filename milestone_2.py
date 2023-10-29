import random
def my_random_choice(seq):
    if not seq:
        raise ValueError ("Sequence cannot be empty)")
    return seq[random.randint(0, len(seq) - 1)]

word_list = ["grapes","strawberries","apples","pears","kiwis"]
print(word_list)
word = my_random_choice(word_list)
print(word)
guess = input("Please enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else: 
    print("Oops! That is not a valid input.")
