def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            
            if board[row][col] != ' ':
                print("Cell already taken! Choose another.")
                continue
            
            board[row][col] = current_player
            
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")

if __name__ == "__main__":
    tic_tac_toe()
