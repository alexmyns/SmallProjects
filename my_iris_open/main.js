input = [2,5,6,9,10]

let minVal = Math.min(input)
let maxVal = Math.max(input)

function findGCD(input){
    for (minVal; minVal <= maxVal; minVal++) {
        if(maxVal% minVal == 0) {
            return minVal
        }
    }
    return 1
}

console.log(findGCD(input))