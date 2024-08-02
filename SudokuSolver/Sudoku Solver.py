#Sudoku Solver
# This is also 1 to 1 follow, I honestly avoid copy paste(I can just do that but..)
# so that I can learn properly while writing the code
# until complete understanding, changes will be made
# according to my preferences 25/7/2024

#2/8/2024
#I modify some changes instead of using pre determined board
#Added func for user input board instead
#Enjoy cheating Sudoku board. lol

from pprint import pprint

#introducing new empty lists to fill it up
a, b, c, d, e, f, g, h, j = [], [], [], [], [], [], [], [], []

# sum up lists for a 9x9 board
board = []
# to show the format for user
example_board = [['a row'],
                 ['b row'],
                 ['c row'],
                 ['d row'],
                 ['e row'],
                 ['f row'],
                 ['g row'],
                 ['h row'],
                 ['j row']]

#function to fill up the lists
def fill_list(name,lst):
    lst.clear()
    for i in range(9):
        try:
            pprint(example_board)
            value = int(input(f'Input number from {name}{i+1}, if blank just press Enter : '))
            lst.append((value) if value != '' else -1)
        except ValueError:
            lst.append(-1)
            
        print(lst)
        if i == 8:
            answer = input(f"All the {name}'s input correct? Y or N?").upper()
            if answer == 'N':
                print("remake the board")
                lst.clear()
                fill_list(name,lst)
            elif answer == 'Y':
                return name,lst
            else:
                print("Invalid input")

#fill the board, run all the function list with name, and list as parameter
def fill_the_board():
# using global to ensure the change made is applied to whole list and also avoid IndexError
    global a, b, c, d, e, f, g, h, j, board

    fill_list('a', a)
    fill_list('b', b)
    fill_list('c', c)
    fill_list('d', d)
    fill_list('e', e)
    fill_list('f', f)
    fill_list('g', g)
    fill_list('h', h)
    fill_list('j', j)

# the board format
    board = [
        [a[0], a[1], a[2],  a[3], a[4], a[5],  a[6], a[7], a[8]],
        [b[0], b[1], b[2],  b[3], b[4], b[5],  b[6], b[7], b[8]],
        [c[0], c[1], c[2],  c[3], c[4], c[5],  c[6], c[7], c[8]],

        [d[0], d[1], d[2],  d[3], d[4], d[5],  d[6], d[7], d[8]],
        [e[0], e[1], e[2],  e[3], e[4], e[5],  e[6], e[7], e[8]],
        [f[0], f[1], f[2],  f[3], f[4], f[5],  f[6], f[7], f[8]],

        [g[0], g[1], g[2],  g[3], g[4], g[5],  g[6], g[7], g[8]],
        [h[0], h[1], h[2],  h[3], h[4], h[5],  h[6], h[7], h[8]],
        [j[0], j[1], j[2],  j[3], j[4], j[5],  j[6], j[7], j[8]]
    ]
    


def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None)) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None # if no spaces in the puzzle are empty (-1) so just return None

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True if is valid, False otherwise

    # let's start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # now the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # and then the square
    # this is tricky, but we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3 # 1 // 3 = 0, 5 // 3 = 1, ...
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    # if we get here, these checks pass
    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1 if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):  # range(1,10) is 1, 2, 3, ...9
        # step 3: check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle !
            puzzle[row][col] = guess
            # now recurse using this puzzle
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
            
        # step 5: if not valid OR if our guess does not solve the puzzle, then we need to
        # backtrack and try a new number
        puzzle[row][col] = -1 # reset the guess

    # step 6 : if none of the numbers that we try work, the this puzzle is UNSOLVABLE
    return False

if __name__ == '__main__':
    fill_the_board()

    # Solve the user-input board
    print("Solving user-input board:")
    if solve_sudoku(board):
        pprint(board)
    else:
        print("No solution exists for the user-input board")