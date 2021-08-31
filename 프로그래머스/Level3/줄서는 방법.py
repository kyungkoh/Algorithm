#0901 
#단순한 permutation 문제 인줄 알았는데, 약간은 복잡한 규칙성 찾기 문제였다. 
#어려웡 ㅠ

import math
def solution(n, k):
    answer = []
    
    numlist = [i for i in range(1,n+1)]
    
    while len(numlist)!=0: 
        temp = math.factorial(n) //n
        index = k // temp
        k = k % temp
        
        if k == 0 : 
            answer.append(numlist.pop(index-1))
        else:
            answer.append(numlist.pop(index))
    
    return answer