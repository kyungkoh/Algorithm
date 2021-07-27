#0726 
#간단한 BFS 문제였다, 왜 Lv3인지 이해가 어렵다

from collections import deque

def solution(n, edge):
    answer = 0
    start = 1 
    
    graph = [[] for _ in range(n+1)]
    dist = [0]*(n+1)
    
    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])    
    
    #print(graph)
    queue = deque([start])
    
    while queue : 
        v = queue.popleft()
        for i in graph[v]:
            if dist[i] == 0:
                dist[i] = dist[v]+1
                queue.append(i)
    
    dist[start] = 0
    
    answer = dist.count(max(dist))
    
    return answer