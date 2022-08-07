#Sudoku Solver.
#Input sudoku board one line at a time to solve up to evil difficulty


import numpy as np
board=[] #create an empty array

print('Sudoku Solver')
print('')
print("Input Board to solve. (Places 0's for empty spaces)")
print('')

#inputting values for each line
c = 0 
while c < 9:
    print('Input row', c+1, 'Enter each value with a space between them')
    val = list(map(int, input().split()))
    if len(val) == 9:
        board.append(val)
    else:
        c -=1 #decrement if list given is not valid
        print('You must have a number for each block')
        print('')
    c +=1

np.reshape(board, (9,9)) #reshape the array into a 9 by 9 board
        

#drawing the board in terminal
def print_board(su):
    for x in range(len(su)):
        if x%3 == 0 and x!=0:
            print("-----------------------")
        for y in range(len(su[0])):
            if y%3 == 0 and y!=0:
                print(" | ", end ="")
            if y==8:
                print(su[x][y])
            else:
                print(str(su[x][y]) + " ",end="")

#checking if a square is empty in the board
def check_empty(su):
    for x in range(len(su)):
        for y in range(len(su[0])):
            if su[x][y] == 0:
                return (x, y)
    return None

#checking for duplicates
def valid(su, num, pos):
    for x in range(len(su[0])):#checking row
        if su[pos[0]][x] == num and pos[1]!= x:
            return False
    for y in range(len(su)):#checking column
        if su[y][pos[1]] == num and pos[0]!= y:
            return False
#checking 3 by 3 box
    box_x = pos[1]//3
    box_y = pos[0]//3
    for x in range(box_y*3, box_y*3 + 3):
        for y in range(box_x*3, box_x*3 + 3):
            if su[x][y] == num and  (x,y) != pos:
                return False
    return True

#solving the board
def solve(su):
    find = check_empty(su)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(su, i , (row,col)):
            su[row][col] = i
            if solve(su):
                return True
            su[row][col]=0
    return False

print('Provided Board')
print('')
print_board(board)
solve(board)
print('')
print('')
print('Solved Board')
print('')
print_board(board)
