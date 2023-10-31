import random


class Hangman:
    def init(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.random_word = random.choice(word_list)
        

        
# Create an instance of the Hangman class
word_list = ["grapes", "strawberries", "apples", "pears", "kiwis"]

hangman_instance = Hangman()

# Access the attributes using the instance

print("word list:", hangman_instance)