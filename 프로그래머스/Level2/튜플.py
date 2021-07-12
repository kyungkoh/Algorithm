#0712

def solution(s):
    answer = []
    
    a = s[2:-2]
    a = a.split('},{')
    
    a.sort(key = len)
    
    for i in a:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))   
    
    return answer