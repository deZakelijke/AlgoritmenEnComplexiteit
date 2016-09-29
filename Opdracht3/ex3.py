# Made by Micha de Groot, september 2016
import sys

def readFile():
    data = [] 
    firstLine = sys.stdin.readline()
    firstLine = firstLine.split()
    data.append(firstLine[1])
    for i in range(int(firstLine[0])):
        nextLine = sys.stdin.readline()
        data.append(nextLine)
    return data

def LCS(answer,test):
    cost = []
    sequence = []
    for i in range(len(answer)+1):
        cost.append([])
        sequence.append([])
        cost[i] = [0]*(len(test)+1)
        sequence[i] = ["0"]*(len(test)+1)
    for i in range(1,len(cost)):
        for j in range(1,len(cost[0])):
            if answer[i-1] == test[j-1]:
                cost[i][j] = cost[i-1][j-1]+1
                sequence[i][j] = sequence[i-1][j-1]+answer[i-1]
            elif cost[i][j-1] > cost[i-1][j]:
                cost[i][j] = cost[i][j-1]
                sequence[i][j] = sequence[i][j-1]
            else:
                cost[i][j] = cost[i-1][j]
                sequence[i][j] = sequence[i-1][j]
    return sequence[-1][-1][1:]

def main():
    data = readFile()
    answer = data[0]
    data = data[1:]
    matches = [[],[]]
    for i in range(len(data)):
        sequence = LCS(answer,data[i])
        matches[0].append(len(sequence))
        matches[1].append(sequence)
    for i in range(len(matches[0])):
        print(matches[0][i],matches[1][i])


main()

    
