#0719 
def solution(s):
    answer = []
    total = 0
    turn = 0
    
    while True:
        cnt=0
        for i in range(len(s)):
            if s[i] == '0':
                cnt+=1
        total +=cnt
        #c = len(s)-cnt
        c = str(bin(len(s)-cnt))[2:]
        s = c
        turn+=1
        if s == '1':
            break
    answer.append(turn)
    answer.append(total)
    return answer