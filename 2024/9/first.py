from functools import reduce


# f = open('/home/max/adventofcode/2024/9/input_test') #1928
# f = open('/home/max/adventofcode/2024/9/test')
f = open('/home/max/adventofcode/2024/9/input') #90180292337
inputText = f.read()
parsedInput = []
for charIndex in range(0, len(inputText), 2):
    value = int(charIndex / 2)
    data = inputText[charIndex:charIndex + 2]
    for i in range(int(data[0])):
        parsedInput.append(value)
    if len(data) == 2:
        for i in range(int(data[1])):
            parsedInput.append('.')
# print(''.join(parsedInput))
charIndex = 0
result = 0
while charIndex < len(parsedInput):
    if parsedInput[charIndex] == '.':
        next = '.'
        while next == '.':
            next = parsedInput.pop()
        parsedInput[charIndex]= next

    result += int(parsedInput[charIndex]) * charIndex
    charIndex += 1
# print(''.join(parsedInput))
print(result)