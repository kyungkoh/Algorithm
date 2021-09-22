#0922
#string 

def solution(s):
    answer = ''
    temp = ''
    word = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            temp += s[i]
            if temp in word:
                idx = word.index(temp)
                answer += str(idx)
                temp = ''
            else:
                continue
            
    return int(answer)