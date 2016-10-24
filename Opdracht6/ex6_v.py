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
        values.update({nextLine[0]: int(nextLine[1])})
    for i in range(int(firstLine[1])):
        nextLine = sys.stdin.readline()
        nextLine = nextLine.split()
        clause = dict()
        for j in range(len(nextLine)):
            if nextLine[j][0] == "~":
                clause.update({nextLine[j][1:]: 0})
            else:
                clause.update({nextLine[j]: 1})
        formula.update({i: clause})
    return values, formula

def checkClause(clause, values):
    valid = False
    for literal in clause:
        if values[literal] == clause[literal]:
            valid = True
    return valid

def main():
    values, formula = readfile()
    for i in range(len(formula)):
        clauseValid = checkClause(formula[i], values)
        if not clauseValid:
            print("Vervult formule niet")
            return
    print("Vervult formule")
    
main()
