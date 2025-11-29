vertex = ['A', 'B', 'C', 'd', 'E']
weight = [[None, 29, None, None, 34],
          [29, None, None, 17, None],
          [None, None, None, None, None],
          [None, 17, None, None, None],
          [34, None, None, None, None]]

def weightSUM(vlist, W):
    sum = 0
    for i in range(len(vlist)):
        for j in range(i + 1, len(vlist)):
            if W[i][j] != None:
                sum += W[i][j]
    return sum

def printAllEdges(vlist, W):
    for i in range(len(vlist)):
        for j in range(i + 1, len(W[i])):
            if W[i][j] != None and W[i][j] != 0:
                print("(%s, %s, %d)" %(vlist[i], vlist[j], W[i][j]), end = ' ')
                

graph = {'A' : {('B', 29), ('F, 10')            },
         'B' : {('A, 29'), ('C', 16), ('G, 15')},
         'C' : {('B', 16), ('D', 12)            },
         'D' : {('C', 12), ('E', 22), ('G', 18)},
         'E' : {('D', 22), ('F', 27), ('G', 25)},
         'F' : {('A', 10), ('E', 27)            },
         'G' : {('B', 15), ('D', 18), ('E', 25)}}

def weightSum(graph):
    sum = 0
    for v in graph:
        for e in graph[v]:
            sum += e[1]
    return sum // 2

def printAllEdge(graph):
    for v in graph:
        for e in graph[v]:
            print("(%s, %s, %d)" %(v, e[0], e[1]), end = ' ')