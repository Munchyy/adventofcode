
f = open('/home/max/adventofcode/2024/7/input')
# f = open('/home/max/adventofcode/2024/7/input_test')
# f = open('/home/max/adventofcode/2024/7/test')
inputText = f.read()

def parseInputLine(line):
    [resultString, numberString] = line.split(': ')
    numberString.split(' ')
    return int(resultString), list(map(lambda n: int(n), numberString.split(' ')))

def workOnLine(target, accumulator, next:list, debugOutput):
    if target < accumulator:
        return False
    if len(next) == 0:
        return target == accumulator
    nextNum = next.pop(0)
    return workOnLine(target, accumulator + nextNum, list(next), debugOutput + ' + ' + str(nextNum)) or \
        workOnLine(target, accumulator * nextNum, list(next), debugOutput + ' * ' + str(nextNum)) or \
        workOnLine(target, int(str(accumulator) + str(nextNum)), list(next), debugOutput + ' || ' + str(nextNum))

result = 0
for line in inputText.splitlines():
    target, numbers = parseInputLine(line)
    first = numbers.pop(0)
    if workOnLine(target, first, numbers, str(first)):
        result += target
print(result)