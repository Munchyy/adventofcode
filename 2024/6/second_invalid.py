# Not checking enough states of an infinite loop, guessing a non square inf is valid?
from enum import Enum
from functools import reduce
import time
test = False
# f = open('/home/max/adventofcode/2024/6/input')
f = open('/home/max/adventofcode/2024/6/input_test') if test else open('/home/max/adventofcode/2024/6/input')
inputText = f.read()
patrolMap = list(map(lambda row: list(row), inputText.splitlines()))

def getStartingCoords():
    global patrolMap
    for rowIndex in range(len(patrolMap)):
        for columnIndex in range(len(patrolMap[0])):
            if patrolMap[rowIndex][columnIndex] == '^':
                return columnIndex, rowIndex
            

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
def turn(direction):
    if direction == Direction.LEFT:
        return Direction.UP
    return Direction(direction.value + 1)

def getNextCoords(currentCoords, direction):
    (currentX, currentY) = currentCoords
    match direction:
        case Direction.UP:
            return (currentX, currentY - 1)
        case Direction.DOWN:
            return (currentX, currentY + 1)
        case Direction.LEFT:
            return (currentX - 1, currentY)
        case Direction.RIGHT:
            return (currentX + 1, currentY)

def getSafe(coords):
    global patrolMap
    (column, row) = coords
    if -1 < column < len(patrolMap[0]) and -1 < row < len(patrolMap):
        return patrolMap[row][column]
    return None

def printMap(count):
    global patrolMap
    for row in patrolMap:
        print(''.join(row))
    print('count: ' + str(count))
    time.sleep(0.1)

def scan(coords, direction):
    (colIndex, rowIndex) = coords;
    currentRow = patrolMap[rowIndex]
    currentCol = list(map(lambda arr: arr[colIndex], patrolMap))
    posBuffer = 1
    negBuffer = 0
    match turn(direction):
        case Direction.UP:
            return '|' in currentCol[:rowIndex + negBuffer] or '+' in currentCol[:rowIndex + negBuffer]#checking up
        case Direction.DOWN:
            return '|' in currentCol[rowIndex + posBuffer:] or '+' in currentCol[rowIndex + posBuffer:]#checking down
        case Direction.LEFT:
            return '-' in currentRow[:colIndex + negBuffer] or '+' in currentRow[:colIndex + negBuffer]#checking left
        case Direction.RIGHT:
            return '-' in currentRow[colIndex + posBuffer:] or '+' in currentRow[colIndex + posBuffer:]#checking right
def setMarker(coords, direction):
    global patrolMap
    current = patrolMap[coords[1]][coords[0]]
    
    if direction in [Direction.LEFT, Direction.RIGHT]:
        marker = '+' if current == '|' else '-'
    else:
        marker = '+' if current == '-' else '|'
    patrolMap[coords[1]][coords[0]] = marker

def patrol():
    currentCoords = getStartingCoords()
    count = 0
    patrolMap[currentCoords[1]][currentCoords[0]] = '|'
    direction = Direction.UP
    while True:
        if test:
            printMap(count)
        nextCoords = getNextCoords(currentCoords, direction)
        next = getSafe(nextCoords)
        if not next:
            return count
        if next == '#':
            direction = turn(direction)
            patrolMap[currentCoords[1]][currentCoords[0]] = '+'
            currentCoords = getNextCoords(currentCoords, direction)
        else:
            if scan(currentCoords, direction):
                count += 1
            setMarker(currentCoords, direction)
            currentCoords = nextCoords
print(patrol())