import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.random_word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.random_word)
        

        
# Create an instance of the Hangman class
list = ["grapes", "strawberries", "apples", "pears", "kiwis"]

hangman_instance = Hangman(list)

# Access the attributes using the instance
print(list)
print("num lives:", hangman_instance.num_lives)
print("word list:", hangman_instance.word_list)
print("random word:", hangman_instance.random_word)


