import sys
while True:
  board = {1: " ", 2: " ", 3: " "
          , 4: " ", 5: " ", 6: " "
          , 7: " ", 8: " ", 9: " "}
  player = "O"
  game = False
  turns = 0
  def print_board():
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print("-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-+-+-")
    print(f"{board[7]}|{board[8]}|{board[9]}")
  while not game:
    print_board()
    print(f"It is player {player}'s turn.\n")
    choice = int(input())
    if choice not in board.keys():
      print("Sorry... That is not in a valid position.")
      continue
    if board[choice] != " ":
      print("Sorry... That cell is already occupied.")
      continue
    board[choice] = player
    turns = turns + 1
  
    if turns == 9:
      print("OK! Now, all the cells have been occupied, so the game has ended with a draw.")
      game = True
  #Row
    for i in range(1, 9, 3):
      if board[i] == board[i+1] == board[i+2] == player:
        print(f"{player} has won the game!")
        game = True
  #Column
    for i in range(1, 4):
      if board[i] == board[i+3] == board[i+6] == player:
        print(f"{player} has won the game!")
        game = True
  #Diagonal     
    if board[1] == board[5] == board[9] == player:
      print(f"{player} has won the game!") 
      game = True
    if board[3] == board[5] == board[7] == player:
      print(f"{player} has won the game!")  
      game = True
    if player == "O":
      player = "X" 
    else: player = "O"
  again = input("If you want to play again, press 'a' on your keyboard.")
  if again != "a":
    break