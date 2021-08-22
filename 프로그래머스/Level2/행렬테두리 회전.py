#0822 Dev_matching 
# 배열을 시뮬레이션 돌리는 문제.. 
# 단순 해 보이는데 왤케 어려운지...
def solution(rows, columns, queries):
    answer = []
    cnt = 1
    graph = [[0 for r in range(columns)] for c in range(rows) ]
    t = 1
    for r in range(rows):
        for c in range(columns):
            graph[r][c] = t
            t+=1
    
    for x1,y1,x2,y2 in queries:
        temp = graph[x1-1][y1-1]
        mini = temp
        
        for q in range(x1-1,x2-1):
            test = graph[q+1][y1-1]
            graph[q][y1-1] = test
            mini = min(mini,test)
        
        for q in range(y1-1,y2-1):
            test = graph[x2-1][q+1]
            graph[x2-1][q] = test
            mini = min(test,mini)
            
        for q in range(x2-1,x1-1,-1):
            test = graph[q-1][y2-1]
            graph[q][y2-1] = test
            mini = min(test,mini)
        
        for q in range(y2-1,y1-1,-1):
            test = graph[x1-1][q-1]
            graph[x1-1][q] = test
            mini = min(test,mini)
            
        graph[x1-1][y1] = temp
        answer.append(mini)
            
    
    
    return answer