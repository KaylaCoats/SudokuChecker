correct = [[8,2,7,1,5,4,3,9,6],
         [9,6,5,3,2,7,1,4,8],
         [3,4,1,6,8,9,7,5,2],
         [5,9,3,4,6,8,2,7,1],
         [4,7,2,5,1,3,6,8,9],
         [6,1,8,9,7,2,4,3,5],
         [7,8,6,2,3,5,9,1,4],
         [1,5,4,7,9,6,8,2,3],
         [2,3,9,8,4,1,5,6,7]]

#incorrectRow
incorrectRow = [[8,2,7,1,5,4,3,9,6],
                [9,6,5,3,2,7,1,4,8],
                [3,3,1,6,8,9,7,5,2],
                [5,9,3,4,6,8,2,7,1],
                [4,7,2,5,1,3,6,8,9],
                [6,1,8,9,7,2,4,3,5],
                [7,8,6,2,3,5,9,1,4],
                [1,5,4,7,9,6,8,2,3],
                [2,4,9,8,4,1,5,6,7]]

#incorrectCol
incorrectCol = [[8,2,7,1,5,4,3,9,6],
                [9,6,5,3,2,7,1,4,8],
                [3,4,1,6,8,9,7,5,2],
                [5,9,3,4,6,8,2,7,1],
                [4,7,2,5,1,3,6,8,9],
                [6,1,8,9,7,2,4,3,5],
                [7,8,6,2,3,5,9,1,4],
                [1,5,4,7,9,6,8,2,3],
                [2,4,9,8,3,1,5,6,7]]

incorrectBlock = [[1,2,3,4,5,6,7,8,9],
                  [9,1,2,3,4,5,6,7,8],
                  [8,9,1,2,3,4,5,6,7],
                  [7,8,9,1,2,3,4,5,6],
                  [6,7,8,9,1,2,3,4,5],
                  [5,6,7,8,9,1,2,3,4],
                  [4,5,6,7,8,9,1,2,3],
                  [3,4,5,6,7,8,9,1,2],
                  [2,3,4,5,6,7,8,9,1]]

def check_sudoku(game):
    n = len(game)
    if n < 1:
        return False
    for i in range(0, n):
        horizontal = []
        vertical = []
        for k in range(0, n):
            #vertical check
            if game[k][i] in vertical:
                print("Failed Vertical Col:",i)
                return False
            vertical.append(game[k][i])

            if game[i][k] in horizontal:
                print("Failed Horizontal Row:",i)
                return False
            horizontal.append(game[i][k])
    
    for checkRow in range(0,n):
        for checkCol in range(0,n):
            blockRow = checkRow // 3
            blockCol = checkCol // 3
            block = []
            
            for row in range(0,n):
                for col in range(0,n):
                    if row // 3 == blockRow and col // 3 == blockCol:
                        if game[row][col] in block:
                            print("Failed Block:",blockRow,blockCol)
                            return False
                        block.append(game[row][col])
    return True

print("Should be Correct")
print(check_sudoku(correct))
print("--Row Check--")
print(check_sudoku(incorrectRow))
print("--Col Check--")
print(check_sudoku(incorrectCol))
print("--Block Check--")
print(check_sudoku(incorrectBlock))
