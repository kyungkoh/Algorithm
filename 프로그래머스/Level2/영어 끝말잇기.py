#210628

def solution(n, words):
    answer = []
    read = []
    cnt  = 1
    read.append(words[0])
    first,second = 0,0
    flag = 0
    
    
    for i in range(1,len(words)):
        if words[i] not in read and words[i-1][-1] == words[i][0]:
            read.append(words[i])
            cnt+=1
        else: 
            first = (i%n)+1
            second = (i//n)+1
            break
    
    return [first,second]