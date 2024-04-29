#This next program is a Blackjack game.

import random
import sys
while True:
  turns = 2
  score1 = 0
  score2 = 0
  for i in range(2):
      x = random.randint(1, 10)
      y = random.randint(1, 10)
      score1 += x
      score2 += y

  print(score1)
  print(score2)

  print("Your draw is", score1)
  print("The computer's draw is", score2)

  while True:
      choice = input("Enter whether you want to hit(h), stand(s), or end(e) the game.")
      if choice == "h":
          turns += 1
          score1 += random.randint(1, 10)
          score2 += random.randint(1, 10)
          print("Your score is", score1)
      elif choice == "s":
          if score1 > score2:
            print("You won!!!")
          elif score2 > score1:
            print("The computer won!")
          else:
            print("It is a draw.")
          break
      elif choice == "e":
          sys.exit()
      if score1 > 21:
          print("You busted and lost all of your money. -( ")
          break
      elif score1 == 21:
          print("You got an exact 21, and you won!")
          break
      if score2 > 21:
          print("The computer busted and lost all of it's money. -(. It got a,", score2)
          break
      elif score2 == 21:
          print("The computer got an exact 21, and it won!")
          break
      if turns >= 5:
        print("Sorry... You have reached your limit. You must now either stand or end the game!")
        break
  choice2 = input("If you want to play again, press a on you keyboard.")
  if choice2 == "a": 
    continue
  else:
    break
