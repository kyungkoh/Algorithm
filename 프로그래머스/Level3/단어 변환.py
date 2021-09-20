#0920
#BFS

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    queue = []
    queue.append((begin,0))
    
    while queue:
        now, depth = queue.pop(0)
        print(now,depth)
        for w in words:
            diff = 0 
            for i in range(len(w)):
                if now[i] != w[i]:
                    diff += 1
            if diff == 1 and w == target:
                depth +=1
                return depth
            elif diff == 1: 
                queue.append((w,depth+1))
                
    answer = depth 
    
    return answer