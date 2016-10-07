# Made by Micha de Groot 10434410

import sys

def readFile():
    studentToThesis = []
    startToStudent = []
    thesisToEnd = []
    firstLine = sys.stdin.readline()
    firstLine = firstLine.split()
    students = int(firstLine[0])
    theses = int(firstLine[1])
    for i in range(int(firstLine[2])):
        nextLine = sys.stdin.readline()
        nextLine = nextLine.split()
        studentToThesis.append([])
        studentToThesis[i].append(int(nextLine[0]))
        studentToThesis[i].append(int(nextLine[1]))
        studentToThesis[i].append(0)
        studentToThesis[i].append(1)
    for i in range(1,students+1):
        startToStudent.append([])
        startToStudent[-1].append(0)
        startToStudent[-1].append(i)
        startToStudent[-1].append(0)
        startToStudent[-1].append(1)
    for i in range(1,theses+1):
        thesisToEnd.append([])
        thesisToEnd[-1].append(i)
        thesisToEnd[-1].append(-1)
        thesisToEnd[-1].append(0)
        thesisToEnd[-1].append(1)
    return studentToThesis, startToStudent, thesisToEnd, students, theses

def findPath(studentToThesis, startToStudent, thesisToEnd):
    firstnode = 0
    lastnode = -1
    for i in range(len(startToStudent)):
        if startToStudent[i][2] == 0:
            for j in range(len(studentToThesis)):
                if studentToThesis[j][2] == 0 and studentToThesis[j][0] == startToStudent[i][1]:
                    for k in range(len(thesisToEnd)):
                        if thesisToEnd[k][2] == 0 and thesisToEnd[k][0] == studentToThesis[j][1]:
                            return [i,j,k]
    return 0
    

def updateData(studentToThesis, startToStudent, thesisToEnd,pathresult):
    startToStudent[pathresult[0]][2] = 1
    studentToThesis[pathresult[1]][2] = 1
    thesisToEnd[pathresult[2]][2] = 1
    return studentToThesis, startToStudent, thesisToEnd
    

def main():
    studentToThesis, startToStudent, thesisToEnd, students,theses = readFile()
    edgesFound =0
    pathresult = 1
    while pathresult:
        pathresult = findPath(studentToThesis, startToStudent, thesisToEnd)
        if pathresult:
            studentToThesis, startToStudent, thesisToEnd = updateData(studentToThesis, startToStudent, thesisToEnd,pathresult)
            edgesFound += 1
    print(edgesFound)
    

    

main()

        
