# Importing the necessary modules
import random
from hangman_words import word_list  # Importing the list of words for the game
from hangman_art import stages, logo  # Importing the ASCII art for the lives and logo

# Display the logo at the start of the game
print(logo)

# Randomly select a word from the word_list
chosen_word = word_list[random.randint(0, (len(word_list) - 1))]
# print(chosen_word)

# Set the initial number of lives
lives = len(stages) - 1

# Create a list to display the guessed letters (initially all underscores)
display = []

# Initialize the display with underscores for each letter in the chosen_word
for letter in chosen_word:
    display.append("_")

# Main game loop, which runs as long as the player has lives remaining
while lives > 0:
    # Prompt the user to guess a letter and convert it to lowercase
    user_guess = input("Guess a letter: ").lower()

    # Check if the user has already guessed the letter
    if user_guess in display:
        print(f"You have already guessed {user_guess}")

    # Check each position in the chosen_word to see if it matches the guessed letter
    for position in range(len(chosen_word)):
        if user_guess == chosen_word[position]:
            display[position] = user_guess
    
    # If the guessed letter is not in the chosen_word, the user loses a life
    if user_guess not in chosen_word:
        print(f"{user_guess} is not one of the letters in the word.\nYou lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose")

    # Display the current state of the guessed letters
    print(f"{' '.join(display)}")

    # If there are no more underscores in the display, the user has won
    if "_" not in display:
        print("You win")

    # Display the current stage of the hangman art based on the number of lives left
    print(stages[lives])