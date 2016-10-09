# Made by Micha de Groot, 10434410

import sys

def readfile():
    data = []
    testCases = int(sys.stdin.readline())
    for i in range(testCases):
        nextLine = sys.stdin.readline()
        nextLine = nextLine.split()
        nextLine = list(map(int, nextLine))
        data.append([])
        data[i].append(nextLine[0])
        data[i].append(nextLine[1])
        data[i].append(nextLine[2])
    return data

def main():
    data = readfile()
    print(data)


main()
