import random

def hangman():
    # List of words to choose from
    word_list = ["python", "hangman", "programming", "computer", "keyboard", "developer", "algorithm"]
    secret_word = random.choice(word_list).lower()
    guessed_letters = []
    attempts_left = 6  # Number of allowed wrong guesses
    
    print("Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters.")
    
    while True:
        # Display current progress (e.g., "_ _ _ _ _")
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())
        
        # Check if player won
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break
        
        # Check if player lost
        if attempts_left == 0:
            print("Game Over! The word was:", secret_word)
            break
        
        # Get player's guess
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print("Correct!")
        else:
            attempts_left -= 1
            print(f"Wrong! You have {attempts_left} attempts left.")
            
            # Optional: Draw hangman (ASCII art)
            if attempts_left == 5:
                print("  O  ")
            elif attempts_left == 4:
                print("  O  ")
                print("  |  ")
            elif attempts_left == 3:
                print("  O  ")
                print(" /|  ")
            elif attempts_left == 2:
                print("  O  ")
                print(" /|\\ ")
            elif attempts_left == 1:
                print("  O  ")
                print(" /|\\ ")
                print(" /   ")
            elif attempts_left == 0:
                print("  O  ")
                print(" /|\\ ")
                print(" / \\ ")
        
        print("\n------------------------\n")

# Start the game
hangman()