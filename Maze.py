from arraystack import arraystack

def isValidPos(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:
        if map[y][x] == '0' or map[y][x] == 'x': #갈 수 있는 칸이거나 출구면 True
            return True
    return False

def DFS():
    print("DFS : ")
    stack = arraystack(100)
    stack.push((0, 1)) #처음엔 시작 위치만.
    
    while not stack.isEmpty():
        here = stack.pop()
        print(here, end = '=>')
        (x, y) = here
        
        if (map[y][x] == 'x'):
            return True #출구로 나감
        
        else:
            map[y][x] = '.' #방문한 곳 표시
            if isValidPos(x, y - 1): #상
                stack.push((x, y - 1)) 
            if isValidPos(x, y + 1): #하
                stack.push((x, y + 1)) 
            if isValidPos(x - 1, y): #좌
                stack.push((x - 1, y)) 
            if isValidPos(x + 1, y): #우
                stack.push((x + 1, y)) 
        print(' 현재 스택 : ', stack)
        
    return False

MAZE_SIZE = 0