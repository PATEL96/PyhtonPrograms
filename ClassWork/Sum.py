# Write a function getSumOfFirstDigit(numList) that takes a list of positive numbers and 
# returns the sum of all the first digit in the list.

def getSumOfFirstDigit(numList):
    n = len(numList)
    sum = 0
    for i in range(n):
        x = str(numList[i])
        sum = sum + int(x[0])
        
    return sum


List = [11,22,55,879,3221,222,449,4]

print(getSumOfFirstDigit(List))