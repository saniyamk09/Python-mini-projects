import random

words = ['computer', 'program', 'software', 'language', 'python', 'project']
word = random.choice(words)
guessed = []
tries = 8

print("Welcome to Hangman!")

while tries >= 0:
    display = ''
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += '_'
    print("Word:", display)

    if display == word:
        print(f"You guessed it! The word was:{word}")
        break

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print("You already guessed that.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        tries -= 1
        print(f"Wrong guess! Tries left:{tries}")

if tries == 0:
    print(f"You lost! The word was:{word}")

input("Game over!")
        
