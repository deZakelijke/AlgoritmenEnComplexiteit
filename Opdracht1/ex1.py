# Only one of 11 to 20 made in python 2, wasn't in the mood to rewrite more than a few lines
import sys

# Reads the test file and converts it to a 2x2 list
def readF():
    f = open('18.txt')
    lineN = 1
    grid = []
    for line in f:
        grid.append([])
        for i in range(0,lineN*3,3): 
            element = int(line[i:i+2])
            grid[lineN-1].append(element)
        lineN += 1
    return grid

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
    print(indexList)
    while sum(indexList) > 0:
        pyrSum = 0
        for i in range(0, len(pyramid)):
            pyrSum += pyramid[i][indexList[i]]
        if pyrSum > maxSum:
            maxSum = pyrSum
        indexList = decrementList(indexList)
    print(maxSum)

main() 
            
