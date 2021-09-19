#0919 
def solution(n, costs):
    
    costs.sort(key = lambda x:x[2])
    routes = set([costs[0][0],costs[0][1]])
    answer = costs[0][2]
    
    while n != len(routes):
        for i,v in enumerate(costs[1:]):
            if v[0] in routes and v[1] in routes:
                continue
            if v[0] in routes or v[1] in routes:
                routes.update([v[0],v[1]])
                answer += v[2]
                costs[i+1] = [-1,-1,-1]
                break

    return answer
