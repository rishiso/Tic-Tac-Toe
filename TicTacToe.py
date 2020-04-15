import time
from copy import deepcopy

game = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]

def show_board():
    s = ""
    for i in game:
        line = " | ".join(i)
        line += "\n"
        s += line
    print(s)

def open_spots(board):
    spots = []
    for i in range(3):
        for i2 in range(3):
            if board[i][i2] == "-":
                spots.append(i * 3 + i2)
    return spots

def player_move():
    move = int(input("Player move: "))
    while move not in open_spots(game):
        move = int(input("Try Again: "))
    game[move // 3][move % 3] = "X"

def minimax(board, is_maximizing):
    evaluate_board = possible_end(board)
    if evaluate_board[0]:
        return [evaluate_board[1], ""]
    best_move = 0
    if is_maximizing:
        best_value = -float("Inf")
        for move in open_spots(board):
            new_board = deepcopy(board)
            new_board[move // 3][move % 3] = "X"
            hypothetical_value = minimax(new_board, not is_maximizing)[0]
            if hypothetical_value > best_value:
                best_value = hypothetical_value
                best_move = move
    else:
        best_value = float("Inf")
        for move in open_spots(board):
            new_board = deepcopy(board)
            new_board[move // 3][move % 3] = "O"
            hypothetical_value = minimax(new_board, not is_maximizing)[0]
            if hypothetical_value < best_value:
                best_value = hypothetical_value
                best_move = move
    return [best_value, best_move]

def computer_move():
    move = minimax(game, False)[1]
    game[move // 3][move % 3] = "O"
    print(f"The computer played a move at {move}.")

def possible_end(board):
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
    if ["X"] * 3 in wins:
        return [True, 1]
    elif ["O"] * 3 in wins:
        return [True, -1]
    elif not open_spots(board):
        return [True, 0]
    else:
        return [False, 0]

def game_over(winner):
    if winner == 1:
        print("-----PLAYER WINS!-----")
    elif winner == -1:
        print("-----COMPUTER WINS!-----")
    else:
        print("-----DRAW!-----")

def main():
    show_board()
    while not possible_end(game)[0]:
        player_move()
        show_board()
        if not possible_end(game)[0]:
            computer_move()
            show_board()
    game_over(possible_end(game)[1])

if __name__ == "__main__":
    print("-----WELCOME TO TIC TAC TOE!-----\n")
    time.sleep(2)
    print("Blank spaces are represented by dashes.")
    time.sleep(2)
    print("Use keys 0-8 to place objects on the board.")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8\n")
    time.sleep(3)
    main()
    response = input("Play Again? (y/n) ")
    print("\n")
    while response == "y":
        game = [["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]]
        main()
        response = input("Play Again? (y/n) ")
        print("\n")

    print("-----THANK YOU FOR PLAYING!-----")
