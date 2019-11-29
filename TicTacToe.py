import random
import time

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def show_board(b):
    for i in b:
        print(i)
    print("\n")

def open_spots(b):
    spots = []
    for i in range(3):
        for i2 in range(3):
            if b[i][i2] == 0:
                spots.append(i * 3 + i2)
    return spots

def player_move():
    move = int(input("Player move: "))
    while move not in open_spots(game):
        move = int(input("Try Again: "))
    game[move // 3][move % 3] = 1

def find_computer_move():
    copy = game
    #Testing for possible win
    for i in open_spots(game):
        copy[i // 3][i % 3] = 2
        if not possible_win(copy):
            copy[i // 3][i % 3] = 0
            return i
        else:
            copy[i // 3][i % 3] = 0
    #Testing for blocking player win
    for i in open_spots(game):
        copy[i // 3][i % 3] = 1
        if not possible_win(copy):
            copy[i // 3][i % 3] = 0
            return i
        else:
            copy[i // 3][i % 3] = 0
    #Place in center
    if game[1][1] == 0:
        return 4
    #Place in corners
    for i in [0, 2, 6, 8]:
        if game[i // 3][i % 3] == 0:
            return i
    return random.choice(open_spots(game))

def computer_move():
    move = find_computer_move()
    game[move // 3][move % 3] = 2
    print(f"The computer played a move at {move}.")

def possible_win(board):
    wins = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [1] * 3 in wins or [2] * 3 in wins or open_spots(board) == []:
        return False
    else:
        return True

def game_over(board):
    wins = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [1] * 3 in wins:
        print("-----PLAYER WINS!-----")
    elif [2] * 3 in wins:
        print("-----COMPUTER WINS!-----")
    else:
        print("-----DRAW!-----")

def main():
    show_board(game)
    while possible_win(game):
        player_move()
        show_board(game)
        if possible_win(game):
            computer_move()
            show_board(game)
    game_over(game)

if __name__ == "__main__":
    print("-----WELCOME TO TIC TAC TOE!-----\n")
    time.sleep(2)
    print("X's are represented with 1, O's are represented with 2, and blank spaces are represented by 0.")
    time.sleep(4)
    print("Input a number from 0-8 to place objects on the board.")
    print("[0, 1, 2]")
    print("[3, 4, 5]")
    print("[6, 7, 8]\n")
    time.sleep(4)
    main()
    response = input("Play Again? (y/n) ")
    print("\n")
    while response == "y":
        game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        main()
        response = input("Play Again? (y/n) ")
        print("\n")

    print("-----THANK YOU FOR PLAYING!-----")
