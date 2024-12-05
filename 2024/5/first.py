from functools import reduce


f = open('/home/max/adventofcode/2024/5/input')
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
def formatPage(pageLine):
    return list(map(lambda item: int(item), pageLine.split(',')))
pages = list(map(formatPage, inputLines[splitter + 1:]))
rules = reduce(rulesToDict, inputLines[:splitter], {})

accumulator = 0
def checkPage(page:list):
    global rules
    global accumulator
    for ruleKey, ruleItems in rules.items():
        if ruleKey in page:
            keyIndex = page.index(ruleKey)
            if keyIndex != -1:
                for ruleItem in ruleItems:
                    if ruleItem in page and page.index(ruleItem) < keyIndex:
                        return
    accumulator += page[int(((len(page) - 1) / 2))]
    
for page in pages:
    checkPage(page)

print(accumulator)