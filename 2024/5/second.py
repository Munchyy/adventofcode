from functools import reduce


f = open('/home/max/adventofcode/2024/5/input')
# f = open('/home/max/adventofcode/2024/5/test')
# f = open('/home/max/adventofcode/2024/5/input_test')
input = f.read()
inputLines = input.splitlines()
splitter = inputLines.index("")
def rulesToDict(acc, curr):
    [a,b] = curr.split('|')
    if int(a) in acc:
        acc[int(a)] = [*acc[int(a)], int(b)]
    else:
        acc[int(a)] = [int(b)]
    return acc
pageNumbersList = list(map(lambda pageLine: list(map(lambda item: int(item), pageLine.split(','))), inputLines[splitter + 1:]))
rules = reduce(rulesToDict, inputLines[:splitter], {})

accumulator = 0
for pageNumbers in pageNumbersList:
    incorrect = False
    for ruleKey, ruleItems in rules.items():
        if ruleKey in pageNumbers:
            keyIndex = pageNumbers.index(ruleKey)
            if keyIndex != -1:
                for ruleItem in ruleItems:
                    if ruleItem in pageNumbers:
                        ruleItemIndex = pageNumbers.index(ruleItem)
                        if ruleItemIndex < keyIndex:
                            incorrect = True
                            pageNumbers = [
                                *pageNumbers[:ruleItemIndex],
                                ruleKey,
                                *pageNumbers[ruleItemIndex:keyIndex],
                                *pageNumbers[keyIndex + 1:]
                            ]
                            keyIndex = ruleItemIndex
    if incorrect:
        accumulator += pageNumbers[int((len(pageNumbers) - 1) / 2)]

print(accumulator)