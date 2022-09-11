import random

play = ["s", "r", "p"]


ok = input("\n\nWelcome to a rock, paper, scissors  python game! Press 'b' on your keyboard to begin.\n")

if ok == "b":
  begin = input("Ok! Let's begin! Enter  '1' to play.\n")

if begin == "1":
  start = input("Ok! Enter 'r' to play rock, 'p' to play paper, and 's to play scissors.\n")
  choice = random.choice(play)

if start == "s":
  print("Rock, paper, scissors, says... SHOOT!")
  print("The computer plays:\n")
  print(random.choice(choice))
  if choice == "s":
    print("It was a draw.")
  elif choice == "p":  
    print("You won! Congrats!")
  elif choice == "r":
    print("The computer won!")

if start == "r":
  print("Rock, paper, scissors, says... SHOOT!")
  print(random.choice(choice))
  if choice == "s":
    print("You won! Congrats!")
  elif choice == "p":  
    print("The computer won!")
  elif choice == "r":
    print("It was a draw.")
  
if start == "p":
  print("Rock, paper, scissors, says... SHOOT!")
  print(random.choice(choice))
  if choice == "s":
    print("The computer won!")
  elif choice == "p":  
    print("It was a draw.")
  elif choice == "r":
    print("You won! Congrats!")














