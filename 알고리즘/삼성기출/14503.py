#1011

#북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def change (d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2


def clean (r,c,d):
    cnt = 1
    x = r
    y = c
    graph[x][y] = 2

    while True:
        dc = d
        for _ in range(4):
            nx = x + dx[dc]
            ny = y + dy[dc]
            dc = change(dc)
            empty = 0 

            if (0<=nx<n and 0<=ny<m and graph[nx][ny] == 0):
                cnt +=1 
                x = nx
                y = ny
                graph[nx][ny] = 2
                d = dc
                empty = 1
                break

        if empty == 0 : 
            if d == 0:
                x+=1
            elif d == 1:
                y-=1
            elif d == 2 :
                x-=1
            elif d == 3:
                y+=1

            if graph[x][y] == 1:
                break

    return cnt



n, m = map(int,input().split())
r,c,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
res = clean(r,c,d)

print(res)