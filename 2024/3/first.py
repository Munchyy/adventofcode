import re


f = open('./input')
# f = open('./test')
input = f.read()
pattern = '(mul\(\d*,\d*\))'
matches = re.findall(pattern, input)

accumulator = 0
for match in matches:
    multPatterm = 'mul\((\d*),(\d*)\)'
    a,b = re.search(multPatterm, match).groups()
    accumulator += int(a) * int(b)

print(accumulator)