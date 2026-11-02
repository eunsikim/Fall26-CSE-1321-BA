def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end="|")
        print()
        print("------")

def main():
    board = [
            [" ", " ", " "], 
            [" ", " ", " "], 
            [" ", " ", " "]
        ]

    print_board(board)
    print("\n")

    board[0][0] = "X"

    print_board(board)
    print("\n")

    board[2][2] = "O"
    
    print_board(board)
    print("\n")

if __name__ == "__main__":
    main()
