#0829 
#stack을 사용한 단순한 구현문제
#주어진 예시만 생각하지 말고 더 많은 테케 생각하기!
from collections import deque

def iskey (k,p):
    if k == '[' and p == ']':
        return True
    elif k == '{' and p =='}':
        return True
    elif k == '(' and p == ')':
        return True
    else: 
        return False

def iscollect(givens):
    stack = []
    for ss in givens:
        if len(stack) == 0 : 
            stack.append(ss)
        else:
            if iskey(str(stack[-1]),ss):
                stack.pop()
            else:
                stack.append(ss)
    if len(stack) == 0 :
        return True
    else:
        return False
            
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        dq = deque(s)
        t = dq.popleft()
        dq.append(t)
        ss = ''.join(dq)
        #print(ss)
        if iscollect(ss) == True:
            answer +=1
        s = ss
    return answer