#This next program is the Hangman game.

import random

words = [
    "catastrophe", "concatenate", "hangman", "random", "capital", "sensitive",
    "competition", "participants", "control", "pneumonia",
    "pneumonoultramicroscopicsilicovolcanoconiosis", "joking", "halfpace",
    "eucalyptus", "scoliosis", "trivial", "inbox", "stuffed", "apple", "orange"
]
word = random.choice(words)
turns = 5
guessed = []
display_word = ""
print("No capital letters. This program is case sensitive.")
print("You have only 4 chances to guess the word.")

for i in word:
    display_word = display_word + "_ "
print(display_word)

while True:
    guess = input("Guess a letter, any letter.\n")
    check = False
    display_word = ""
    if len(guess) > 1:
        print("Sorry... You can only guess one letter at a time.")
        continue
    if guess in guessed:
        print("You've already guessed that certain letter.")
        continue
    if guess in word:
        print("You guessed a letter correctly.")
        guessed.append(guess)
    else:
        print("You guessed that letter wrong.")
        print(turns)
        turns = turns - 1
        if turns == 0:
            print("Sorry, you are out of turns. Your word was", word, ".")
            choice = input(
                "If you want to play again, press 'a' on your keyboard.")
            if choice == "a":
              word = random.choice(words)
              guessed = []
              turns = 5
              continue
            else:
                break
    for i in word:
        if i in guessed:
            display_word = display_word + i + " "
        else:
            display_word = display_word + "_ "
            check = True
    if check == False:
        print("You word was", word)
        print("You have guessed the word! Congrats!")
        choice = input(
            "If you want to play again, press 'a' on your keyboard.")
        if choice == "a":
            word = random.choice(words)
            guessed = []
            turns = 5
            continue
        else:
            break
        break
    print(display_word)
