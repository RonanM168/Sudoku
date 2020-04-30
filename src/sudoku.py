def readBoard (file):

	infile = open(file, "r")
	b = []
	for line in infile:
		newline = line.strip("\n")
		row = newline.split(" ")
		intRow = []
		for sNum in row:
			intRow.append(int(sNum))
		b.append(intRow)


	infile.close()
	return b

def printBoard (SBoard):
	for rowNo in range (9):
		if rowNo % 3 == 0:
			print ("+---------+---------+---------+")
		for colNo in range (9):
			if colNo % 3 == 0:
				print ("|", end="")
			if SBoard[rowNo][colNo] == 0:
				print ("   ", end="")
			else:
				print (" %i " % (SBoard[rowNo][colNo]), end="")
		print ("|")
	print ("+---------+---------+---------+")

def solveBoard (b, row, col):
    #directing the program to the next cell in the grid which you want to address by moving through the columns and rows
    if col<8:
        nextRow = row
        nextCol = col + 1
    else:
        nextRow = row + 1
        nextCol = 0
    #checking if you have filled each cell in the grid and solved the problem
    if row>=9:
        return True,b
    #filling in each cell of the grid with the correct values
    else:
        #if the number is already in the grid, move on to the next cell
        if b[row][col] != 0:
            return solveBoard(b, nextRow, nextCol)
        #if the cell is empty, finding the correct value
        else:
            #checking each value from 1 to 9 to see if it is a valid move
            for number in range(1, 10):
                #if it is a valid move, place this number in the grid
                if isValidMove(b, row, col, number):
                    b[row][col]=number
                    #checking if there is a number that can possibly be placed in the next cell and if there is, continuing to fill in the cells
                    res = solveBoard(b, nextRow, nextCol)
                    if res[0] == True:
                        return True, b
            #if no valid number can be placed in the cell, delete the value in the previous cell
            b[row][col]=0
        #returning false to the function and trying again with a different value
        return False, b



#defining a function to check if the move is valid
def isValidMove (b, row, col, number):
    #setting the initial answer to true
    valid = True
    #checking if the number is already in the row using indices and setting the result to false if it is not
    if number in b[row]:
        valid = False
        return  valid

    #checking if the number is already in the column using indices and setting the result to false if it is not
    for i in range(9):
        if board[i][col] == number:
            valid = False
            return  valid
    #checking if the number is already in the 3x3 grid using floor division and setting the result to false if it is not
    y=row//3 *3
    x=col//3 *3
    for p in range(y, y+3):
        for q in range(x, x+3):
            if b[p][q] == number:
                valid = False
                return valid

    #returning the answer
    return valid

#Main Program
filename = "easyPuzzle.txt"
board = readBoard (filename)

print ("\nPROBLEM:")
printBoard (board)


result, solvedBoard = solveBoard (board, 0, 0)
if result == False:
    print ("Solution does not exist")
else:
    print ("\nSOLUTION:")
    printBoard (solvedBoard)
