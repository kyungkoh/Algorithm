#0720
from collections import deque
n,m = map(int,input().split())

graph = [] 
for i in range(n):
    graph.append(list(map(int,input())))

#이동 할 방향 정의 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    #큐가 빌 때 까지 반복 
    while queue :
        x,y = queue.popleft()
        #현재 방향에서 네방향 확인 
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #범위를 벗어 난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #벽인 경우 무시 
            if graph[nx][ny] == 0: 
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))
