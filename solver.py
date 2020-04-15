problem_board = [
    [4,0,0,0,9,6,0,0,8],
    [0,5,9,0,2,4,0,0,6],
    [0,6,0,3,0,0,0,9,4],
    [0,0,2,0,0,0,0,6,0],
    [6,8,0,0,0,0,4,5,1],
    [0,7,0,0,0,0,0,8,0],
    [8,1,5,4,0,0,6,2,7],
    [7,0,0,0,0,0,8,0,0],
    [2,0,0,0,6,8,0,1,5]
]

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j

    return None

def solved(board):
    find = find_empty(board)
    if not find:
        return True
    row, col = find
    for num in range(1,10):
        if valid_board(board, num, row, col):
            board[row][col] = num
            if solved(board):
                return True
            board[row][col] = 0
    return False

def valid_board(board, num, row, col):
    for i in range(len(board)):
        if board[i][col] == num and i != row:
            return False

    for i in range(len(board[row])):
        if board[row][i] == num and i != col:
            return False

    row_grid = row // 3
    col_grid = col // 3

    for i in range(row_grid*3, row_grid*3 + 3):
        for j in range(col_grid*3, col_grid*3 + 3):
            if board[i][j] == num and i != row and j != col:
                return False

    return True

def print_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " " , end="")

print_board(problem_board)
solved(problem_board)
print("===================================")
print_board(problem_board)