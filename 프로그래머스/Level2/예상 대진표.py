#0722

def solution(n,a,b):
    answer = 0

    while True: 
        if a != b: 
            answer+=1
            a,b = (a+1)//2,(b+1)//2
        else:
            break
    
    return answer