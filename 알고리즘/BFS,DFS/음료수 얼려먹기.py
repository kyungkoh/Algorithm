#0719

n,m = map(int,input().split())

graph =[]

for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        #상하좌우를 재귀적 호출 
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        return True
    return False

result = 0 

for i in range(n):
    for j in range(m):
        #현재위치에서 dfs 수행
        if dfs(i,j)==True:
            result+=1

print(result)
