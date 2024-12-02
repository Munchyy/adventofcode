# THIS FILE DOESNT WORK BUT HERE FOR IDEAS
# TRIED TO TO MORE INTELLIGENT DAMPING THAN "RERUN WITH INDEX REMOVED" BUT IT GOT MESSY
from functools import reduce


# f = open('./input_test')
# f = open('./input')
f = open('/home/max/adventofcode/2024/2/test')
input = f.read()
inputLines = list(map(lambda item: item.split(' '), input.splitlines()))

def isComparisonSafe(first, second, third, increasing, dampened):
    difference = second - first
    if increasing:
        if difference < 1 or difference > 3:
            if dampened:
                return False, dampened
            else:
                return isComparisonSafe(first, third, None, increasing, True)
    else:
        if difference > -1 or difference < -3:
            if dampened:
                return False, dampened
            else:
                return isComparisonSafe(first, third, None, increasing, True)
    return True, dampened

def isLineSafe(inputLine):
    increasing = int(inputLine[0]) < int(inputLine[len(inputLine) - 1])
    dampened = False
    x = 0
    while x < len(inputLine) - 2:
        isSafe, wasDampened = isComparisonSafe(int(inputLine[x]), int(inputLine[x + 1]), int(inputLine[x + 2]), increasing, False)
        if not isSafe:
            return False
        if wasDampened and not dampened:
            dampened = True
            x += 2
        else: 
            x += 1
    return True

count = 0
for line in inputLines:
    if isLineSafe(line) == True:
        count += 1
print(count)