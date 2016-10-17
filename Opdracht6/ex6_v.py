# Made by Micha de Groot, 10434410

import sys

def readfile():
    values = dict()
    formula = dict()
    firstLine = sys.stdin.readline()
    firstLine = firstLine.split()
    for i in range(int(firstLine[0])):
        nextLine = sys.stdin.readline()
        nextLine = nextLine.split()
        print(nextLine)
        values =values + {nextLine[0]: int(nextLine[1])}
    print(values)
    for i in range(int(fisrLine[1])):
        nextLine = sys.stdin.readline()
        nextLine = nextLine.split()
        formula = formula + {}
        for j in range(len(nextLine)):
            if nextLine[j][0] == "~":
                print("yo")


readfile()

    
