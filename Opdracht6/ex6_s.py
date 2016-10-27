import sys
from collections import OrderedDict


def readfile():
    values = OrderedDict()
    formula = []
    firstLine = sys.stdin.readline()
    firstLine = firstLine.split()
    outputSave = []
    for i in range(int(firstLine[0])):
        nextLine = sys.stdin.readline()
        splitLine = nextLine.split()
        values.update({splitLine[0]: None})
    for i in range(int(firstLine[1])):
        nextLine = sys.stdin.readline()
        outputSave.append(nextLine[:-1])
        splitLine = nextLine.split()
        clause = OrderedDict()
        for j in range(len(splitLine)):
            if splitLine[j][0] == "~":
                #clause.update({splitLine[j][1:]: 0})
                clause[splitLine[j][1:]] = 0
            else:
                #clause.update({splitLine[j]: 1})
                clause[splitLine[j]] = 1
        # sortedClause = OrderedDict(sorted(clause.items(), key=lambda x: x[0]))
        formula.append(clause)
    return [int(firstLine[0]), int(firstLine[1])], values, formula, outputSave

# Voor in het archief
# Godverdomme, heb hier alsnog geen kut aan
'''
def resolutionStep(formula):
    newClause = OrderedDict()
    i = 0
    for clause in formula:
        i +=1
        for literal in clause:
            for compareClause in formula[i:]:
                if literal in compareClause:
                    if clause[literal] != compareClause[literal]:
                        newClause.update(clause)
                        newClause.update(compareClause)
                        newClause.pop(literal)
                        temp = doubleCheck(clause, compareClause, literal)
                        if temp:
                            newClause.pop(temp)
                        if newClause == {}:
                            print(formula)
                            print("Niet vervulbaar")
                            exit()
                # ouwe niet weggooien, maar checken ofer geen dubbelen ontstaan
                        sortedClause = OrderedDict(sorted(newClause.items(), key=lambda x: x[0]))
                        if not (sortedClause in formula):
                            #formula.append(newClause)
                            print("New: ", sortedClause)
                            return sortedClause
    return 0

def doubleCheck(clause1, clause2, oldLiteral):
    for literal in clause1:
        if not literal == oldLiteral:
            if literal in clause2:
                if clause1[literal] != clause2[literal]:
                    return literal
    return 0


    
def assignvalue(values, formula):
    for literal in values:
        for clause in formula:
            if literal in clause:
                values[literal] = clause[literal]
    return values
    '''

def consistent(formula, values):
    for clause in formula:
        clauseB = False
        for literal in clause:
            if literal in values:
                if clause[literal] == values[literal] or values[literal] == None:
                    clauseB = True
        if not clauseB:
            return False
    return True

def valuesNone(values):
    for literal in values:
        if values[literal] == None:
            return literal
    return 0

def assignRecursive(formula, values):
    if not consistent(formula, values):
        return False
    noneIndex = valuesNone(values)
    if not noneIndex:
        return True
    tempValues = values
    tempValues[noneIndex] = 1
    if assignRecursive(formula, tempValues):
        values[noneIndex] = 1
        return True
    else:
        tempValues[noneIndex] = 0
        if assignRecursive(formula, tempValues):
            values[noneIndex] = 0
            return True
        else:
            values[noneIndex] = None
            return False


def main():
    header, values, formula, output = readfile()
    assignRecursive(formula, values)
    if None in values.values():
        print("Niet Vervulbaar")
        exit()

    print(header[0], header[1])
    for literal in values:
        print(literal, values[literal])
    for clause in output:
        print(clause)
main()
