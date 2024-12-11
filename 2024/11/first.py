class LinkedStone:
    def __init__(self, value:int, next):
        self.value = value
        self.next = next
    
    def unused_action(self, actionString):
        match actionString:
            case 'engrave':
                return self.engrave
            case 'split':
                return self.split
            case _:
                return self.doDefault

    def action(self):
        return self.engrave()

    def engrave(self):
        if self.value == 0:
            self.value = 1
            return self.next
        return self.split()
    
    def split(self):
        valueString = str(self.value)
        if len(valueString) % 2 == 0:
            halfWay = int(len(valueString)/2)
            first = int(valueString[:halfWay])
            second = int(valueString[halfWay:])
            self.value = first
            newNext = LinkedStone(second, self.next)
            self.next = newNext
            return newNext.next
        return self.doDefault()

    def doDefault(self):
        self.value *= 2024
        return self.next

# f = open('/home/max/adventofcode/2024/11/input_test') 
# f = open('/home/max/adventofcode/2024/11/test')
f = open('/home/max/adventofcode/2024/11/input') 
inputText = f.read()
values = list(map(lambda item: int(item), inputText.split(' ')))

first = LinkedStone(values.pop(), None)
while len(values):
    first = LinkedStone(values.pop(), first)

def blink():
    global first
    current = first
    while True:
        next = current.action()
        if not next:
            break
        current = next

def debugPrint():
    global first
    current = first
    out = []
    while True:
        out.append(str(current.value))
        if not current.next:
            break
        current = current.next
    print(' '.join(out))

# blinkCount = 75 # TOO LONG!
blinkCount = 25
for _ in range(blinkCount):
    blink()
    # debugPrint()


count = 0
current = first
while True:
    count += 1
    if not current.next:
        break
    current = current.next
print(count)