
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
def addVector(vec1, vec2):
    return (vec1[0] + vec2[0], vec1[1] + vec2[1])
def isVectorInbounds(vec):
    global colCount
    global rowCount
    return vec[0] in range(rowCount) and vec[1] in range(colCount)

accumulator = 0
antinodes = []
for key, values in satMap.items():
    while len(values) > 1:
        firstNode = values.pop(0)
        for secondNode in values:
            diffVector = subtractVector(firstNode, secondNode)
            aNode1 = addVector(firstNode, diffVector)
            if isVectorInbounds(aNode1):
                if not aNode1 in antinodes:
                    antinodes.append(aNode1)
                    accumulator += 1
            aNode2 = subtractVector(secondNode, diffVector)
            if isVectorInbounds(aNode2):
                if not aNode2 in antinodes:
                    antinodes.append(aNode2)
                    accumulator += 1

def printDebug():
    global lines
    global antinodes
    for y in range(len(lines)):
        currOut = ''
        for x in range(len(lines[0])):
            currOut += '#' if (y,x) in antinodes else lines[y][x]
        print(currOut)

# printDebug()
print(accumulator)
