from functools import reduce


# f = open('./input_test')
f = open('./input')
# f = open('/home/max/adventofcode/2024/2/test')
input = f.read()
inputLines = list(map(lambda item: item.split(' '), input.splitlines()))

def isIncreasing(inputNumbers):
    # This didnt work in the case that the last index is dampened, e.g. 2 3 4 5 6 7 1
    # return inputNumbers[0] < inputNumbers[len(inputNumbers) - 1]
    return inputNumbers[0] < (sum(inputNumbers) / len(inputNumbers))

def isSafe(inputLine):
    inputNumbers = list(map(lambda item : int(item), inputLine))
    increasing = isIncreasing(inputNumbers)
    
    for x in range(len(inputNumbers) - 1):
        difference = inputNumbers[x + 1] - inputNumbers[x]
        if increasing:
            if difference < 1 or difference > 3:
                return False, x
        else:
            if difference > -1 or difference < -3:
                return False, x
    return True, None

count = 0
for line in inputLines:
    safe, badIndex = isSafe(line)
    # when encountering a bad index, you can either remove the current or next index to resolve
    if not safe:
        safe, _ = isSafe(line[:badIndex] + line[badIndex+1:])
    if not safe:
        safe, _ = isSafe(line[:badIndex+1] + line[badIndex+2:])
    if safe:
        count += 1
    line
print(count)