#0812
#bfs,dfs
#dfs를 재귀로 안풀고, stack으로만 풀었다. 사실 dfs는 stack으로 구현못하면서 그냥 껴맞춤 ㅋㅋ 바보같다 

def solution(tickets):
    answer = []
    
    routes = {}
    tickets.sort()
    
    print(tickets)
    
    for t1,t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    print(routes)
    
    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0 :
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop(0))
    
   # print(path[::-1])
        
    
    answer = path[::-1]
    return answer