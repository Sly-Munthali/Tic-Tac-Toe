# Creating TicTacToe Mark I
# Because why not, every programmer seems to do it

#Instructions on how to play
Instructions = '''
Here are some instructions on how to play the game

    Board layout
    
   1 | 2 | 3
  ---|---|---
   4 | 5 | 6
  ---|---|---
   7 | 8 | 9
   
-> select a number 1-9 that corressponds with the space you wish to place your mark
-> Player one goes first. . . duh

'''
# Creating the Game Board
game_board = []
for i in range(9):
    game_board.append(' ')

# Print board
def print_board():
    board = f"""
    
    {game_board[0]} | {game_board[1]} | {game_board[2]}
   ---|---|---
    {game_board[3]} | {game_board[4]} | {game_board[5]}
   ---|---|---
    {game_board[6]} | {game_board[7]} | {game_board[8]}

    """
    print(board)

# If user doesn't input between 1-9, redirect to previious state
index_list = []
def take_input(player_name):
    while True:
        X = int(input(f"{player_name}: "))
        X -= 1
        if 0 <= X < 10:
            if X in index_list:
                print("This spot is bloacked.")
                continue
            index_list.append(X)
            return X
        print("Please enter a number between 1-9")


#Asking players for name input
def main():
    print("Welcome, care to play a game of Tic Tac Toe?")
    player_one = input("Enter player one name: ")
    player_two = input("Enter player two name: ")
    print(f"Thank you for joining the game, {player_one} and {player_two} ")

    print(Instructions)
    print(f"{player_one} will be asigned X and {player_two} is O")
    input("Enter any key to start the game: ")



    for number in range(9):
        if number % 2 == 0:
            index = take_input(player_one)
            game_board[index] = 'X'
        else:
            index = take_input(player_two)
            game_board[index] = 'O'

        print_board()




main()