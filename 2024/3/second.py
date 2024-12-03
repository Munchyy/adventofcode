import re


f = open('./input')
# f = open('./input_test')
input = f.read()
pattern = '(mul\(\d*,\d*\))|(do\(\))|(don\'t\(\))'
matches = re.findall(pattern, input)

active = True
accumulator = 0
for match in matches:
    mult, doCommand, dontCommand = match
    if dontCommand:
        active = False
    if doCommand:
        active = True
    if not active or not mult:
        continue

    multPatterm = 'mul\((\d*),(\d*)\)'
    a,b = re.search(multPatterm, mult).groups()
    accumulator += int(a) * int(b)

print(accumulator)