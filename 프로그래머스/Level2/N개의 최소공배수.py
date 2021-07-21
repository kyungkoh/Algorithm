#0721
from math import gcd

def lcm (x,y):
    return x*y//gcd(x,y)

def solution(arr):
    answer = 0
    temp = [] 
    temp.append(arr.pop(0))
    
    while True: 
        temp.append(lcm(temp.pop(0),arr.pop(0)))
        
        if len(arr)==0:
            break
    
    answer = temp[0]
        
    
    return answer