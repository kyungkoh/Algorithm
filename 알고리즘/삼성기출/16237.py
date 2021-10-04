#1004 아기상어 
from collections import deque
INF = 1e9

n = int(input())

array = [] 
for i in range(n):
    array.append(list(map(int,input().split())))

nowx , nowy = 0,0
nowsize = 2

#아기상어가 있는 위치를 찾는다
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            nowx , nowy = i,j
            array[nowx][nowy] = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

#최단거리를 찾는 BFS 함수 
def bfs():
    dist = [[-1]* n for _ in range(n)]
    q = deque([(nowx,nowy)])
    dist[nowx][nowy] = 0 

    while q : 
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<n :
                # 지나간 적이 없거나 아기상어의 크기가 물고기보다 크면 지나갈 수 있음
                if dist[nx][ny] == -1 and array[nx][ny] <= nowsize:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist


#최단거리 테이블이 주어졌을 때 먹을 물고기를 찾는 함수 
def find(dist):
    x,y = 0,0
    min_dist = INF

    for i in range(n):
        for j in range(n):
            #도달 할 수 있는 거리 이면서, 먹을 수 있는 물고기 일때 
            if dist[i][j] != -1 and 1<= array[i][j] < nowsize:
                if dist[i][j] < min_dist:
                    x,y = i,j 
                    min_dist = dist[i][j]
    
    if min_dist == INF:
        return None
    else: 
        return x,y,min_dist

res = 0 
ate = 0 

while True:
    value = find(bfs())

    if value == None:
        print(res)
        break
    else:
        nowx, nowy = value[0], value[1]
        res += value[2]
        array[nowx][nowy] = 0 
        ate+=1

        if ate >= nowsize : 
            nowsize +=1
            ate =0 