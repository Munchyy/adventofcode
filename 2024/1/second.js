const fs = require('fs')
let col1 = []
let col2 = []

const getOccurenceCount = (item, list) =>
    list.filter((listItem) => listItem === item).length

fs.readFileSync(__dirname + '/first_input', 'utf8')
    .split('\n')
    .forEach((line, index) => {
        const [a, b] = line.split('   ')
        col1.push(a)
        col2.push(b)
    })

const out = col1.reduce((acc, curr) => {
    return acc + curr * getOccurenceCount(curr, col2)
}, 0)

console.log(out)
