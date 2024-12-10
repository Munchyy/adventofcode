# f = open('/home/max/adventofcode/2024/10/input_test')
# f = open('/home/max/adventofcode/2024/10/test')
f = open('/home/max/adventofcode/2024/10/input')
inputText = f.read()


def getMatrix():
    global inputText
    inputMatrix = []
    for line in inputText.splitlines():
        inputMatrix.append(list(line))
    return inputMatrix

inputMatrix = getMatrix();

def debug(coords):
    global inputMatrix
    for row in range(len(inputMatrix)):
        out = ''
        for col in range(len(inputMatrix[0])):
            out += "_" if row == coords[0] and col == coords[1] else inputMatrix[row][col]
        print(out)

def getSafe(coords):
    (row, col) = coords
    if 0 <= row < len(inputMatrix) and 0 <= col < len(inputMatrix[0]):
        return -1 if inputMatrix[row][col] == '.' else int(inputMatrix[row][col])
    return None

def recurse(coords, seeking):
    global inputMatrix
    (currentRow, currentCol) = coords
    # debug(coords)
    if seeking == 10:
        inputMatrix[currentRow][currentCol] = '.'
        return 1
    tally = 0
    #LEFT
    if getSafe((currentRow, currentCol - 1)) == seeking:
        inputMatrix[currentRow][currentCol] = '.'
        tally += recurse((currentRow, currentCol - 1), seeking + 1)
    # UP
    if getSafe((currentRow - 1, currentCol)) == seeking:
        inputMatrix[currentRow][currentCol] = '.'
        tally += recurse((currentRow - 1, currentCol), seeking + 1)
    #RIGHT
    if getSafe((currentRow, currentCol + 1)) == seeking:
        inputMatrix[currentRow][currentCol] = '.'
        tally += recurse((currentRow, currentCol + 1), seeking + 1)
    #DOWN
    if getSafe((currentRow + 1, currentCol)) == seeking:
        inputMatrix[currentRow][currentCol] = '.'
        tally += recurse((currentRow + 1, currentCol), seeking + 1)
    return tally

#for each 0
result = 0
for rowIndex in range(len(inputMatrix)):
    for colIndex in range(len(inputMatrix[0])):
        if inputMatrix[rowIndex][colIndex] == '0':
            result += recurse((rowIndex, colIndex), 1)
            inputMatrix = getMatrix();

# val = recurse((0,2), 1)
# print('found: ' + str(val))
# result += val
print(result)

