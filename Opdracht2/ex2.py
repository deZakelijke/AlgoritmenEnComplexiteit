# Made by Micha de Groot
# Algoritmen en Complexiteit Opdracht 2

import sys
import fileinput

# Read the input file
def readF():
    data = []
    lineN=0
    for line in fileinput.input():
        data.append([])
        line = line.split()
        for i in range(len(line)):
            data[lineN].append(int(line[i]))
        lineN +=1
    return data

# Taken from stackoverflow
# sort the edges by length
def sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x[2] < pivot[2]:
                less.append(x)
            if x[2] == pivot[2]:
                equal.append(x)
            if x[2] > pivot[2]:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal not pivot
    else:  # You need to hande the part at the end of the recursion 
        return array

# Find the next shortest edge that expands the grap
def nextEdge(edges,validEdges,visited):
    for i in range(len(edges)):
        if (not(edges[i][0] in visited)) and (edges[i][1] in visited):
            return edges[i],edges[i][0]
        elif (edges[i][0] in visited) and (not(edges[i][1] in visited)):
            return edges[i], edges[i][1]

# Find the shortest network based on the inputdata
def findNetwork(edges, nrNodes, nrEdges):
    validEdges = []
    visited = [0]
    while(len(visited) < nrNodes):
        newEdge, newNode = nextEdge(edges,validEdges,visited)
        validEdges.append(newEdge)
        edges.remove(newEdge)
        visited.append(newNode)
    return validEdges

def main():
    data = readF()
    nodes = data[0][0]
    edges = data[0][1] 
    sorteddata = sort(data[1:edges])
    edgeList = findNetwork(sorteddata,nodes,edges)
    edgeSum = 0
    for i in range(len(edgeList)):
        edgeSum += edgeList[i][2]
    print(edgeSum)

main()
