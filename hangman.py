import random

words = ["python", "codealpha", "cat", "dog", "phone"]
word = random.choice(words)

guessed = []
wrong = 0
max_wrong = 6

print("Hangman, guess the word!")

while wrong < max_wrong:
    revealed = ""
    for letter in word:
        if letter in guessed:
            revealed = revealed + letter + " "
        else:
            revealed = revealed + "_ "
    print(revealed)

    if "_" not in revealed:
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Type only one letter")
        continue

    if guess in guessed:
        print("You already guessed that")
        continue

    guessed.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        wrong = wrong + 1
        print("Wrong! You have only", max_wrong - wrong, "tries left")

if wrong == max_wrong:
    print("You lost. The right word was:", word)
