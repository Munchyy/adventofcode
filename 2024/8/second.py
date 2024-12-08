
f = open('/home/max/adventofcode/2024/8/input')
# f = open('/home/max/adventofcode/2024/8/input_test')
# f = open('/home/max/adventofcode/2024/8/test')
inputText = f.read()

lines = inputText.splitlines()
rowCount = len(lines)
colCount = len(lines[0])
satMap = {}
for rowIndex in range(rowCount):
    for columnIndex in range(colCount):
        curr = lines[rowIndex][columnIndex]
        if curr != '.':
            if curr in satMap:
                satMap[curr].append((rowIndex, columnIndex))
            else:
                satMap[curr] = [(rowIndex, columnIndex)]

def subtractVector(vec1, vec2):
    return (vec1[0] - vec2[0], vec1[1] - vec2[1])


accumulator = 0
antinodes = []

# check for each dimension, if mult is the same, then they are on same line
def checkPointDistanceMult(start, end, factor):
    if factor == 0:
        if start == end:
            return True, 0
        return False, None
    distance = end - start
    return True, distance / factor

def checkOnLine(start, end, lineVector):
    yCheckOk, yRatio = checkPointDistanceMult(start[0], end[0], lineVector[0])
    xCheckOk, xRatio = checkPointDistanceMult(start[1], end[1], lineVector[1])
    # yCheckOK and xCheckOk could be false if factor is 0 and coord is not the same (divide by 0 otherwise)
    return yCheckOk and xCheckOk and yRatio == xRatio
    
def checkCell(y,x):
    global satMap, lines
    if lines[y][x] != '.' and len(satMap[lines[y][x]]) > 1:
            return True
    for frequencyLocations in satMap.values():
        for freqIndex in range(len(frequencyLocations)):
            distanceVector = subtractVector(frequencyLocations[freqIndex], (y,x))
            for frequencyToCheck in frequencyLocations[freqIndex+1:]:
                if checkOnLine((y,x), frequencyToCheck, distanceVector):
                    return True
                continue
    return False
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if checkCell(y,x):
            antinodes.append((y,x))
            accumulator += 1
        



def printDebug():
    global lines
    global antinodes
    for y in range(len(lines)):
        currOut = ''
        for x in range(len(lines[0])):
            currOut += '#' if (y,x) in antinodes and lines[y][x] == '.' else lines[y][x]
        print(currOut)

printDebug()
print(accumulator)

