import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.random_word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.random_word)
        self.list_letters = []  # List to keep track of guessed letters
        self.num_letters = len(set(self.random_word))  # Calculate the number of unique letters
        self.list_of_guesses = []  # List to keep track of guesses

    def display_word_guessed(self):
        return ' '.join(self.word_guessed)

    def guess_letter(self, letter):
        letter = letter.lower()  # Convert letter to lowercase
        if letter in self.list_letters:
            print("You already guessed this letter.")
            return

        if letter in self.random_word:
            for i in range(len(self.random_word)):
                if self.random_word[i] == letter:
                    self.word_guessed[i] = letter
            self.list_letters.append(letter)
        else:
            self.list_letters.append(letter)
            self.num_lives -= 1

        self.list_of_guesses.append(letter)

        
# Create an instance of the Hangman class
list = ["grapes", "strawberries", "apples", "pears", "kiwis"]

hangman_instance = Hangman(list)

# Access the attributes using the instance
print(list)
print("num lives:", hangman_instance.num_lives)
print("word list:", hangman_instance.word_list)
print("random word:", hangman_instance.random_word)
print("Initial Word Guessed:", hangman_instance.display_word_guessed())
print("Updated Word Guessed:", hangman_instance.display_word_guessed())
