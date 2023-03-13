val = "MCMXCIV"

def change(current):
    currentValue = 0
    match current:
        case "I":
            currentValue = 1
        case "V":
            currentValue = 5
        case "X":
            currentValue = 10
        case "L":
            currentValue = 50
        case "C":
            currentValue = 100
        case "D":
            currentValue = 500
        case "M":
            currentValue = 1000
    return currentValue

def romanToInteger(value):
    sum = 0
    nextValue = 0
    for i in range(len(value)):
        currentValue = change(value[i])
        if i+1 < len(value):
            nextValue = change(value[i+1])         
        if currentValue >= nextValue:
            sum+=currentValue
        else:
            sum-=currentValue
    return sum
        

print(romanToInteger(val))