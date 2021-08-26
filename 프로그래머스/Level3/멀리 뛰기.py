#0827 
#단순한 DP 문제 

def solution(n):
    answer = 0
    
    d = []
    d.append(1)
    d.append(2)
    
    for i in range(2,n+1):
        #print(d[i-1]+d[i-2])
        d.append(d[i-1] + d[i-2])
    
    answer = d[n-1]%1234567
    
    return answer