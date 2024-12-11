
# f = open('/home/max/adventofcode/2024/11/input_test') 
# f = open('/home/max/adventofcode/2024/11/test')
f = open('/home/max/adventofcode/2024/11/input') 
inputText = f.read()
values = list(map(lambda item: int(item), inputText.split(' ')))

def valuesToMap(valueArr):
    currMap = {}
    for value in values:
        if value in currMap:
            currMap[value] += 1
        else:
            currMap[value] = 1
    return currMap

def safeAdd(currMap, value, countToAdd):
    if value in currMap:
        currMap[value] += countToAdd
    else:
        currMap[value] = countToAdd
def blink(currMap):
    newMap = {}
    for value, count in currMap.items():
        if value == 0:
            safeAdd(newMap, 1, count)
        elif len(str(value)) % 2 == 0:
            valueString = str(value)
            halfWay = int(len(valueString)/2)
            first = int(valueString[:halfWay])
            second = int(valueString[halfWay:])
            safeAdd(newMap, first, count)
            safeAdd(newMap, second, count)
        else:
            safeAdd(newMap, value * 2024, count)
    # print(newMap)
    return newMap

# def blink():
#     global values
#     index = 0
#     while index < len(values):
#         value = values[index]
#         if value == 0:
#             values[index] = 1
#         elif len(str(value)) % 2 == 0:
#             valueString = str(value)
#             halfWay = int(len(valueString)/2)
#             first = int(valueString[:halfWay])
#             second = int(valueString[halfWay:])
#             values[index] = second
#             values.insert(index, first)
#             index += 1
#         else:
#             values[index] *= 2024
#         index += 1

blinkCount = 75
currMap = valuesToMap(values)
for index in range(blinkCount):
    currMap = blink(currMap)
    
print(str(sum(currMap.values())))