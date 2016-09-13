# Only one of 11 to 20 made in python 2, wasn't in the mood to rewrite more than a few lines
import sys
import fileinput

# Reads the test file and converts it to a 2x2 list
def readF():
    lineN = 1
    grid = []
    for line in fileinput.input():
        grid.append([])
        for i in range(0,lineN*3,3): 
            element = int(line[i:i+2])
            grid[lineN-1].append(element)
        lineN += 1
    return grid

# Takes as input two consecutive lines of the pyramid 
# Compares adjacent elements of the lower line and sums it with the element 'above' it in the pyramid
# Returns a line same length as the upper line of the pyramid
def newSumLine(upperLine,lowerLine):
    sumList = []
    for i in range(len(upperLine)):
        if(lowerLine[i] > lowerLine[i+1]):
            sumList.append(lowerLine[i]+upperLine[i])
        else:
            sumList.append(lowerLine[i+1]+upperLine[i])
    return sumList

# Reads the pyramid from the input file
# Loops through all lines of the pyramid and calculates the highes sum path
def main():
    pyramid = readF()
    pyramidLength = len(pyramid)
    sumLine = pyramid[pyramidLength-1]
    for i in range(pyramidLength-2,-1,-1):
        sumLine = newSumLine(pyramid[i],sumLine)
    print(sumLine[0])

main() 
            
'''
Old brute force method
# decrements the index list to the next iteration of indices
def decrementList(indexList):
    if sum(indexList) <= 0:
        sys.exit('index list below zero error')
    # The exact ssequence that is followed is kinda hard to explain in a few lines so I won't
    # Great comment. I should work on that
    
    for i in range(len(indexList)-1,-1,-1):
        if indexList[i] > indexList[i-1]:
            indexList[i] -= 1
            for j in range(i,len(indexList)-1):
               indexList[j+1] = indexList[j] +1 
            break 
    return indexList


def main():
    pyramid = readF()
    maxSum = 0
    indexList = list(range(0,len(pyramid)))
    while sum(indexList) > 0:
        pyrSum = 0
        for i in range(0, len(pyramid)):
            pyrSum += pyramid[i][indexList[i]]
        if pyrSum > maxSum:
            maxSum = pyrSum
        indexList = decrementList(indexList)
    print(maxSum, end="")
'''

