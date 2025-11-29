def DFS(vtx, adj, s, visited):
    print(vtx[s], end = ' ')
    visited[s] = True
    
    for v in range(len(vtx)):
        if visited[v] == False:
            DFS(vtx, adj, v, visited)
            
from queue import Queue

def BFS_AL(vtx, aList, s):
    n = len(vtx)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        s = Q.get()
        print(vtx[s], end = ' ')
        for v in aList[s]:
            if visited[v] == False:
                Q.put(v)
                visited[v] = True
                
def DFS2(graph, v, visited):
    if v not in visited:
        visited.add(v)
        print(v, end = ' ')
        nbr = graph[v] - visited
        for u in nbr:
            DFS2(graph, u, visited)
            
            
from queue import Queue

def bfs_cc(vtx, adj, s, visited):
    group = [s]
    Q = Queue()
    Q.puts(s)
    visited[s] = True
    while not Q.empty():
        s = Q.get()
        for v in range(len(vtx)):
            if visited[v] == False and adj[s][v] != 0:
                Q.put(v)
                visited[v] = True
                group.append(v)
    return group
            
def find_connected_component(vtx, adj):
    n = len(vtx)
    visited = [False] * n
    groups = []
    
    for v in range(n):
        if visited[v] == False:
            color = bfs_cc(vtx, adj, v, visited)
            groups.append(color)
            
    return groups

def ST_DFS(vtx, adj, s, visited):
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                print("(", vtx[s], vtx[v], ")", end = '')
                ST_DFS(vtx, adj, v, visited)
                