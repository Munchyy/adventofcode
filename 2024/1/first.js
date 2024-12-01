const fs = require('fs')
let col1 = []
let col2 = []

fs.readFileSync(__dirname + '/first_input', 'utf8')
    .split('\n')
    .forEach((line, index) => {
        const [a, b] = line.split('   ')
        col1.push(a)
        col2.push(b)
    })

col1.sort()
col2.sort()

const out = col1.reduce((acc, curr, index) => {
    return acc + Math.abs(+curr - +col2[index])
}, 0)

console.log(out)
