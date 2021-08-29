#0830
#단순한 Floyd Warshall 알고리즘
#효율성을 보고 범위를 최대한 줄여서 봤어야 하는 문제이다. 
def solution(n, s, a, b, fares):
    
    INF = 999999999
    graph = [[INF]*n for _ in range(n)]
    
    for i in range(n):
        graph [i][i]  = 0 
    
    for i in fares:
        graph[i[0]-1][i[1]-1] = i[2]
        graph[i[1]-1][i[0]-1] = i[2]
        
    for t in range(n):
        for i in range(n):
            for j in range(i,n):
                if i != j : 
                    temp = min(graph[i][j],graph[i][t]+graph[t][j])
                    graph[i][j] = graph[j][i] = temp
    
    answer = INF
    
    for t in range(n):
        temp = graph [s-1][t]+graph[t][b-1]+graph[t][a-1]
        answer = min(answer,temp)
    
    return answer