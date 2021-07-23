# 백준 18352
from collections import deque
import sys

input = sys.stdin.readline
n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화 
dist = [-1]*(n+1)
dist[x] = 0 # 출발도시까지의 거리는 0

# bfs 수행
q = deque([x])

while q:
    v = q.popleft()
    
    for i in graph[v]:
        if dist[i] == -1:
            #최단 거리 갱신
            dist[i] = dist[v]+1
            q.append(i)

#print(dist)

fflag = False

for i in range(1,n+1):
    if dist[i] == k:
        print(i)
        fflag = True

if fflag == False:
    print(-1)