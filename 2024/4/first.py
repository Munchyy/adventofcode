from enum import Enum


# f = open('/home/max/adventofcode/2024/4/input_test')
# f = open('/home/max/adventofcode/2024/4/test')
f = open('/home/max/adventofcode/2024/4/input')
input = f.read()
inputLines = input.splitlines()
lineLength = len(inputLines[0])

def safeGet(a, b):
    if 0 <= a < len(inputLines) and 0 <= b < lineLength:
        return inputLines[a][b]
    return ''

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UP_LEFT = 5
    UP_RIGHT = 6
    DOWN_LEFT = 7
    DOWN_RIGHT = 8

chars = ['X', 'M', 'A', 'S', 'DONE']
def nextChar(char):
    if not char:
        return 'x'
    return chars[chars.index(char) + 1]

def nextCoords(x, y, direction):
    if direction == Direction.UP:
        return x - 1, y
    elif direction == Direction.DOWN:
        return x + 1, y
    elif direction == Direction.LEFT:
        return x, y - 1
    elif direction == Direction.RIGHT:
        return x, y + 1
    elif direction == Direction.UP_LEFT:
        return x - 1, y - 1
    elif direction == Direction.UP_RIGHT:
        return x - 1, y + 1
    elif direction == Direction.DOWN_LEFT:
        return x + 1, y - 1
    else:
        return x + 1, y + 1

accumulator = 0
def explore(char, a, b, direction):
    global accumulator
    (nextA, nextB) = nextCoords(a, b, direction)
    if nextChar(char) == 'DONE':
        accumulator += 1
        return
    if not safeGet:
        return
    if safeGet(nextA, nextB) == nextChar(char):
        explore(nextChar(char), nextA, nextB, direction)


for a in range(0, len(inputLines)):
    for b in range(0, lineLength):
        char = safeGet(a,b)
        if char == 'X':
            for directionIndex in range(1, 9):
                explore(char, a, b, Direction(directionIndex))
                
print(accumulator)