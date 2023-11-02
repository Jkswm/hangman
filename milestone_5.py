import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.random_word = random.choice(word_list)
        self.updated_word_guessed = ['_'] * len(self.random_word)
        self.list_letters = []  # List to keep track of guessed letters
        self.num_letters = len(set(self.random_word))  
        self.list_of_guesses = []  

    def display_word_guessed(self):
        return ' '.join(self.updated_word_guessed)

    def guess_letter(self, letter):
        letter = letter.lower()  # Convert letter to lowercase

        if letter in self.list_letters:
            print("You already guessed this letter.")
            return

        correct_guess = any(self.random_word[i] == letter for i in range(len(self.random_word)))

        if correct_guess:
            for i in range(len(self.random_word)):
                if self.random_word[i] == letter:
                    self.updated_word_guessed[i] = letter
        else:
            self.num_lives -= 1

        self.list_letters.append(letter)
        self.list_of_guesses.append(letter)

    def check_guess(self, guess):
        if guess in self.random_word:
            print("You guessed", guess)
            print(f"Good guess! '{guess}' is in the word")
            for i in range(len(self.random_word)):
                if self.random_word[i] == guess:
                    self.updated_word_guessed[i] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            if self.num_lives == 0:
                print("Game over! You've run out of lives.")
                return True  # Return True to indicate that the game is over

    def ask_for_input(self):
        while self.num_lives > 0 and '_' in self.updated_word_guessed:  # Continue while lives > 0 and word not fully guessed
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    game_over = self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    print("Updated Word Guessed:", hangman_instance.display_word_guessed())
                    if not game_over:
                        print(f"You have {self.num_lives} lives left.")
                    else:
                        break  # Exit the loop if the game is over
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
        
        if '_' not in self.updated_word_guessed:
            print("Congratulations! You've guessed the word:", self.random_word)
            

# Create an instance of the Hangman class
word_list = ["grapes", "strawberries", "apples", "pears", "kiwis"]
hangman_instance = Hangman(word_list)

# Access the attributes using the instance
print("num lives:", hangman_instance.num_lives)
print("word list:", hangman_instance.word_list)
print("random word:", hangman_instance.random_word)
print("")
hangman_instance.ask_for_input()




def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        if game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break
           
    
play_game(word_list)