#0813 
#순열로 푸는 문제, 완탐이긴 했는데 가끔 완탐으로 다 풀어야 할지 조합이나 순열로 풀어놓고 풀어야 할지 
#구현 방식에 대해서 정답은 없지만, 자꾸 고민된다...
from itertools import permutations

def is_match(user,banned_id):
    for i in range(len(user)):
        if len(user[i]) != len(banned_id[i]):
            return False
        for j in range(len(user[i])):
            if banned_id[i][j] == "*":
                continue
            elif user[i][j] != banned_id[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    ans = []
    answer = 0
    
    user_set = list(permutations(user_id,len(banned_id)))
    
    for user in user_set:
        if is_match(user,banned_id):
            user = set(user)
            if user not in ans:
                ans.append(user)
    
    answer = len(ans)
    
    return answer