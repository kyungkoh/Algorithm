from itertools import combinations
# 후보키
# 어려워.. 
def solution(relation):
    answer = 0
    
    n_col = len(relation[0])
    n_row = len(relation)
    
    combi = [] 
    #모든 키의 집합을 구함
    for i in range(1,n_col+1):
        combi.extend(combinations(range(n_col),i))
    
    final = []
    
    # 유일성 만족
    for keys in combi:
        temp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(temp)) == n_row:
            final.append(keys)
            
    #최소성 만족      
    answer = set(final[:])
    
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(final[i])==len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
                
    #print(answer)
    return len(answer)