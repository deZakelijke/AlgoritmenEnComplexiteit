import sys


def readfile():
    values = dict()
    formula = []
    firstLine = sys.stdin.readline()
    firstLine = firstLine.split()
    outputSave = []
    for i in range(int(firstLine[0])):
        nextLine = sys.stdin.readline()
        nextLine = nextLine.split()
        values.update({nextLine[0]: None})
    for i in range(int(firstLine[1])):
        nextLine = sys.stdin.readline()
        outputSave.append(nextLine[:-1])
        nextLine = nextLine.split()
        clause = dict()
        for j in range(len(nextLine)):
            if nextLine[j][0] == "~":
                clause.update({nextLine[j][1:]: 0})
            else:
                clause.update({nextLine[j]: 1})
        formula.append(clause)
    return [int(firstLine[0]), int(firstLine[1])], values, formula, outputSave

def resolutionStep(formula):
    newClause = dict()
    i = 0
    for clause in formula:
        i +=1
        for literal in clause:
            for compareClause in formula[i:]:
                if literal in compareClause:
                    if clause[literal] != compareClause[literal]:
                        print("Clause: ", clause)
                        print("comp: ", compareClause)
                        newClause.update(clause)
                        newClause.update(compareClause)
                        newClause.pop(literal)
                        print("New: ", newClause)
                        if newClause == {}:
                            print("Niet vervulbaar")
                            exit()
                        formula.remove(clause)
                        formula.remove(compareClause)
                        formula.append(newClause)
                        return formula
    return 0

def assignvalue(values, formula):
    for literal in values:
        for clause in formula:
            if literal in clause:
                values[literal] = clause[literal]
    return values

def main():
    header, values, formula, output = readfile()
    for i in range(10):
        update= resolutionStep(formula)
        if update:
            formula = update
        else:
            break
    values = assignvalue(values, formula)

    '''
    print(header[0], header[1])
    for literal in values:
        if values[literal] == None:
            print(literal, 1)
        else:
            print(literal, values[literal])
    for clause in output:
        print(clause)
    '''
    
main()
