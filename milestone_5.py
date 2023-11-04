import random
# Define a class of Hangman
class HangmanGame:
    def __init__(self, word_list, num_lives=5): # Initialises the game
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ['_' if letter.isalpha() else letter for letter in self.word] # Creates a list to represent the word going to be guessed and uses '_' to represent the unguessed letters
        self.num_letters = len(set(self.word) - set(self.list_of_guesses)) # Calculates the number of distinct letters in the word that have not been guessed yet 

# Method checks if the guess is in the word
    def check_letter(self, letter):
        if letter in self.word: # If the letter is in the word it replaces'_' with the letter in the word_guessed
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
                    self.num_letters -= 1
            return True
        else: # If the letter is not in the word, reduce the number of lives and give feedback
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            return False
 # Method asks the player for their input (letter they want to check is in the word)
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_letter(guess)
                self.list_of_guesses.append(guess)
            # Shows the current status of the game
            print("Word guessed so far:", ' '.join(self.word_guessed))
            print("Lives left:", self.num_lives)
            print("Letters already guessed:", ' '.join(self.list_of_guesses))

            if self.num_lives <= 0:
                print("You've run out of lives! The word was:", self.word)
                break

            if '_' not in self.word_guessed:
                print("Congratulations! You've guessed the word:", self.word)
                break
#Function that plays the Hangman game
def play_game(word_list):
    num_lives = 5
    game = HangmanGame(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break
# Entry point for running the Hangman game
if __name__ == "__main__":
    word_list = ["grapes", "strawberries", "apples", "pears", "kiwis"]
    play_game(word_list)
