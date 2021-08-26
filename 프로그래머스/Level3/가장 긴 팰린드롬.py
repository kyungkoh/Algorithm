#0827

def isPalindrome(x):
    if x == x[::-1]:
        return True

def solution(s):
    answer = 0
    Max = 0
    for i in range(len(s)):
        for j in range(i,len(s)+1):
            if isPalindrome(s[i:j]):
                if Max < len(s[i:j]):
                    Max = len(s[i:j])
    
    answer = Max
    
    return answer