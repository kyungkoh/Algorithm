#0719
from itertools import permutations
import math

def isPrime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
    return True

def solution(numbers):
    answer = 0
    arr = []
    arr2 = []
    num = 0
    
    for i in range(1,len(numbers)+1):
        arr = list(permutations(numbers,i))
        for j in range(len(arr)):
            num = int(''.join(map(str,arr[j])))
            if isPrime(num):
                arr2.append(num)
                
    arr2 = list(set(arr2))            
    answer = len(arr2)
    
        
    return answer