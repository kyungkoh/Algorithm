#bfs

from collections import deque

def bfs (n,computers,start,visited):
    queue = deque([start])
    visited[start] = True
    
    while queue: 
        v = queue.popleft()
        visited[v] = True
        for con in range(n):
            if con != v and computers[v][con] == 1:
                if visited[con] == False:
                    queue.append(con)

def solution(n, computers):
    answer = 0    
    visited = [False]*n
    
    for com in range(n):
        if visited[com] == False:
            bfs(n,computers,com,visited)
            answer+=1
            
    return answer