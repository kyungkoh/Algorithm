#0716

def solution(clothes):
    answer = 1
    
    dic = {}
    
    for element in clothes:
        key = element[1] 
        value = element [0]
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value] 
    
    for i in dic:
        print(len(dic[i])+1)
        answer *= (len(dic[i])+1)
    
    return answer-1