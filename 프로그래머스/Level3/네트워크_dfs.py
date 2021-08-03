#dfs

def dfs(n,computers,start,visited):
    visited[start] = True
    
    for com in range(n):
        if com != start and computers[start][com] ==1 : #연결된 컴퓨터 
            if visited[com]== False:
                dfs(n,computers,com,visited)
            

def solution(n, computers):
    answer = 0    
    visited = [False] * n
    
    for com in range(n):
        if visited[com] == False:
            dfs(n,computers,com,visited)
            answer+=1
            
    return answer