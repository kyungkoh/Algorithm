#0802
#규칙을 찾아야하는 문제.. 
def solution(msg):
    answer = []
    
    alpha = {}
    
    for i in range(1,27):
        alpha[chr(i+64)] = i
    
    w, c = 0,0
    
    while True:
        c+=1
        if c == len(msg):
            answer.append(alpha[msg[w:c]])
            break
        if msg[w:c+1] not in alpha:
            alpha[msg[w:c+1]] = len(alpha)+1
            answer.append(alpha[msg[w:c]])
            w = c
        
    return answer