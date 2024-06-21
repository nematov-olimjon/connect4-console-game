ROWS = 6
COLUMNS = 7
EMPTY = " "
PLAYER_1 = "X"
PLAYER_2 = "O"

board = [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]


def print_board():
    for row in board:
        print("|" + "|".join(row) + "|")
    print(" " + "-" * (COLUMNS * 2 - 1))


def check_winner(player: str) -> bool:
    # here we are checking horizontally if there is a winner
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if (board[row][col] == player and board[row][col + 1] == player
                    and board[row][col + 2] == player and board[row][col + 3] == player):
                return True
    # here we are checking vertically if there is a winner
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if (board[row][col] == player and board[row + 1][col] == player
                    and board[row + 2][col] == player and board[row + 3][col] == player):
                return True
    # here we are checking diagonally if there is a winner
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if (board[row][col] == player and board[row + 1][col + 1] == player
                    and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player):
                return True
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if (board[row][col] == player and board[row - 1][col + 1] == player
                    and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player):
                return True
    return False


def move(player: str, column: int) -> bool:
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == EMPTY:
            board[row][column] = player
            return True
    return False


def main():
    current_player = PLAYER_1
    while True:
        print_board()
        print(f"\nPlayer {current_player}'s turn.")
        try:
            column = int(input("Input column (0-6): "))
            if column < 0 or column >= COLUMNS:
                print("Invalid column. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not move(current_player, column):
            print("Column is full. Try another one.")
            continue

        if check_winner(current_player):
            print_board()
            print(f"Player with {current_player} wins!")
            break

        current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1

    print("Game over!!!")


if __name__ == "__main__":
    main()
