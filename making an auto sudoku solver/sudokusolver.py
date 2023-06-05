# Load the Sudoku board from file
with open("sdk.txt", "r") as file:
    lines = file.readlines()

board = []
for line in lines:
    row = [int(num) for num in line.split()]
    board.append(row)

def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, num, pos):
    # Periksa baris
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Periksa kolom
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Periksa kotak 3x3
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve_sudoku(board):
    empty = find_empty(board)

    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

# Function to solve the Sudoku using the solve_sudoku function from the previous example
def solve():
    solve_sudoku(board)

# Solve the Sudoku
solve()

# Save the solved Sudoku to file
with open("sdkrslt.txt", "w") as file:
    for row in board:
        file.write(" ".join(str(num) for num in row))
        file.write("\n")
