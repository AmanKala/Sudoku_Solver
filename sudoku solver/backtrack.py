import time

# Represents the Sudoku board (Problem statement)

board = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]

# Function to print the board

def display_board(brd):
    for row in range (len(brd)):
        if row % 3 == 0 and row != 0:
            print('----------------------')

        for column in range (len(brd[row])):
            if column % 3 == 0 and column != 0:
                print("| ", end = "")                           # used ' end = "" ' to keep the cursor on the same line

            if column == 8:
                print(brd[row][column])
            else:
                print(str(brd[row][column]) + " ", end = "")


# Function to check the valid entry of number

def check(brd, num_row, num_column, entry):

    # For checking in the small 3*3 matrix
    matrix_i = num_row // 3
    matrix_j = num_column // 3
    for i in range(matrix_i * 3, matrix_i * 3 + 3):
        for j in range(matrix_j * 3, matrix_j * 3 + 3):
            if brd[i][j] == entry and i != num_row and j != num_column:
                return False

    # For checking along the column
    for row in range(len(brd)):
        if brd[row][num_column] == entry and row != num_row:
            return False

    # For checking along the row
    for column in range(len(brd[num_row])):
        if brd[num_row][column] == entry and column != num_column:
            return False

    return True


# Function to solve the board by backtracking algorithm

def solve_board(brd):
    global count
    count += 1

    row, column = -1, -1
    for i in range(len(brd)):
        for j in range(len(brd[i])):
            if brd[i][j] == 0:
                row, column = i, j
                break
        if row != -1:
            break

    if row == -1:                                       # Base Statement
        return True

    for i in range(9):
        if check(brd, row, column, i+1):
            brd[row][column] = i+1

            if solve_board(brd):                        # Recursive statement
                return True

            brd[row][column] = 0
    return False


# Function to solve the board by backtracking algorithm and show the STEP BY STEP solution

def solve_board_and_show(brd):
    print("\n")
    global count
    count += 1
    time.sleep(.5)
    display_board(brd)

    row, column = -1, -1
    for i in range(len(brd)):
        for j in range(len(brd[i])):
            if brd[i][j] == 0:
                row, column = i, j
                break
        if row != -1:
            break

    if row == -1:
        return True                                              # Base Statement

    for i in range(9):
        if check(brd, row, column, i+1):
            brd[row][column] = i+1

            if solve_board_and_show(brd):                        # Recursive statement
                return True

            brd[row][column] = 0
    return False



count = 0
print("\n\nWELCOME TO THE SUDOKU SOLVER \n\n")
print("The initial board is :- ")
display_board(board)
choice = input("\n\n Would you like to see a STEP BY STEP SOLUTION ? (yes/no) ")
ans = True

if choice == 'yes':
    ans = solve_board_and_show(board)

else:
    ans = solve_board(board)

print("\n \n")

if ans:
    print("The  final solution of the board is :- \n")
    display_board(board)
    print("\nNUMBER OF CALLS OF THE RECURSIVE FUNCTION = ", count)
else:
    print("There is NO VALID SOLUTION ")


