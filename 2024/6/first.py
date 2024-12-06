from enum import Enum
from functools import reduce
import time

# f = open('/home/max/adventofcode/2024/6/input')
f = open('/home/max/adventofcode/2024/6/input_test')
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

def printMap():
    global patrolMap
    for row in patrolMap:
        print(''.join(row))
def patrol():
    currentCoords = getStartingCoords()
    pathCount = 0
    direction = Direction.UP
    while True:
        # printMap()
        nextCoords = getNextCoords(currentCoords, direction)
        next = getSafe(nextCoords)
        if not next:
            return pathCount + 1
        if next == '#':
            direction = turn(direction)
        else:
            if next == '.':
                pathCount += 1
            patrolMap[currentCoords[1]][currentCoords[0]] = 'X'
            patrolMap[nextCoords[1]][nextCoords[0]] = '^'
            currentCoords = nextCoords
print(patrol())