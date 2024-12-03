import re


f = open('./input')
input = f.read()

nums = ['0','1','2','3','4','5','6','7','8','9']
matchList = ['m', 'u', 'l', '(']

command, multA, multB, firstNum = ('', '', '', True)

accumulator = 0
for char in input:
    if len(command) < 4 and matchList[len(command)] == char:
        command += char
        continue
    elif len(command) == 4:
        if char in nums:
            if firstNum:
                multA += char
            else:
                multB += char
            continue
        elif char == ',':
            if firstNum:
                firstNum = False
                continue
        elif char == ')' and len(multA) != 0 and len(multB) != 0:
            accumulator += int(multA) * int(multB)
            command, multA, multB, firstNum = ('', '', '', True)
    command, multA, multB, firstNum = ('', '', '', True)

        
print(accumulator)