#0827
#배열의 원소의 곱이 최대가 되려면 각 숫자간의 범위가 적어야한다.
def solution(n, s):
    answer = []
    if n > s: 
        answer = [-1]
    else: 
        div = s//n
        mod = s%n
        for _ in range(n):
            answer.append(div)
        for i in range(mod):
            answer[i]+=1
            
        answer.sort()
            
    return answer