from functools import reduce


# f = open('./input_test')
f = open('./input')
# f = open('./test')
input = f.read()
inputLines = list(map(lambda item: item.split(' '), input.splitlines()))

def isSafe(inputLine):
    increasing = int(inputLine[0]) < int(inputLine[len(inputLine) - 1])
    
    for x in range(len(inputLine) - 1):
        difference = int(inputLine[x + 1]) - int(inputLine[x])
        if increasing:
            if difference < 1 or difference > 3:
                return False
        else:
            if difference > -1 or difference < -3:
                return False
    return True

count = 0
for line in inputLines:
    if isSafe(line) == True:
        count += 1
print(count)