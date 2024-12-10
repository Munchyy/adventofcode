from functools import reduce
def debugPrint(input):
    out = []
    for item in input:
        for _ in range(item['length']):
            value = item['value']
            out.append('.' if value == None else str(value))
    print(''.join(out))

# f = open('/home/max/adventofcode/2024/9/input_test') #2858
# f = open('/home/max/adventofcode/2024/9/test')
f = open('/home/max/adventofcode/2024/9/input') #6379678017108 wrong (too high) #6379677752410
inputText = f.read()
maxValue = -1
parsedInput = []
# change input to dict list for ease
for charIndex in range(0, len(inputText), 2):
    value = int(charIndex / 2)
    data = inputText[charIndex:charIndex + 2]
    maxValue = value
    parsedInput.append({
        "value": value,
        "length": int(data[0])
    })
    if len(data) == 2:
        parsedInput.append({
            "value": None,
            "length": int(data[1])
        })
# for each block of data, go descending values (avoids index changes from insertions)
for currentValue in range(maxValue, -1, -1):
    # get index in list to be able to move it (is there a counterpart of JS .find(item => item.value === currentValue?)
    for itemIndex in range(len(parsedInput)):
        if parsedInput[itemIndex]['value'] == currentValue:
            break
    item = parsedInput[itemIndex]
    for checkIndex in range(itemIndex):
        toCheck = parsedInput[checkIndex]
        if toCheck['value'] == None:
            if toCheck['length'] != 0 and toCheck['length'] >= item['length']:
                # we have found a gap that fits (doesnt matter if we leave a gap of 0)
                toCheck['length'] -= item['length']
                toInsert = parsedInput.pop(itemIndex)
                parsedInput.insert(checkIndex, toInsert)
                # concat spaces left from removal (e.g {...}{11}{...} should change to {........} in the dict list)
                newGap = {"value": None, "length": toInsert['length']}
                # check any gap after popped item
                if parsedInput[itemIndex]['value'] == None:
                    newGap['length'] += parsedInput.pop(itemIndex)['length']
                # check any gap before popped item
                if parsedInput[itemIndex-1]['value'] == None: # use if there is one, else make a new gap
                    parsedInput[itemIndex-1]['length'] += newGap['length']
                else:
                    parsedInput.insert(itemIndex, newGap)
                # debugPrint(parsedInput)
                break
# debugPrint(parsedInput)

# expand parsedInput items into array to work on
outArr = []
for item in parsedInput:
    for _ in range(item['length']):
        outArr.append(0 if item['value'] == None else item['value'])
# work on array
result = 0
for i in range(len(outArr)):
    result += outArr[i] * i
print(result)



# result = 0
# for itemIndex in range(len(parsedInput)):
#     item = parsedInput[itemIndex]
#     if item['value'] != None:
#         result
