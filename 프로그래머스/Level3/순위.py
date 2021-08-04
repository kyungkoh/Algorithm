#0805 
#set의 문법과 명제에 대해서 다시 생각해볼 만한 문제였다. 

def solution(n, results):
    answer = 0
    
    #wins[key] : 이긴 사람들의 집합
    #loses[key] : 진 사람들의 집합
    
    wins, loses = {},{}
    
    for i in range(1,n+1):
        wins[i], loses[i] = set(),set()
    
    for i in range(1,n+1):
        for res in results:
            if res[0] == i: 
                wins[i].add(res[1])
            if res[1] == i: 
                loses[i].add(res[0])
        #print("wins ",wins,"loses ",loses)
        #i를 이긴 사람들 (lose[i]) => i에게 진 사람 (wins[i])은 반드시 이긴다
        for winner in loses[i]:
            wins[winner].update(wins[i])
        #i에게 진 사람들 (wins[i]) => i를 이긴 사람들(loses[i])에게는 반드시 진다
        for loser in wins[i]:
            loses[loser].update(loses[i])
    
    #print("wins ",wins,"loses ",loses)
    
    for i in range(1,n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            answer+=1
        
    
    
    
    return answer