#0915
#단순한 구현 문제이지만, key를 돌리는 것을 구현하는 것과 자물쇠를 3배로 늘리는 풀이는 
#빠르게 생각하기 쉽지 않을 듯하다

def turn_dic(a):
    n = len(a) #행 길이 
    m = len(a[0])
    
    result = [[0]*n for _ in range(m)]
    
    for i in range (n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    
    return result  

def check(new_lock):
    lock_len = len(new_lock)//3
    
    for i in range(lock_len,lock_len*2):
        for j in range(lock_len,lock_len*2):
            if new_lock[i][j] != 1:
                return False
    return True
            

def solution(key, lock):
    answer = True
    #자물쇠 크기
    N = len(lock[0])
    #열쇠 크기 
    M = len(key[0])
    
    # 자물쇠를 3배 크기로 만든다    
    new_lock = [[0]*(N*3) for _ in range(N*3)]
    # 큰 자물쇠 중간에 원래 자물쇠 모형을 넣는다. 
    for i in range(N):
        for j in range(N):
            new_lock[i+N][j+N] = lock[i][j]    
    
    
    #4가지 방향에 대해서 확인한다. 
    
    for dic in range(4):
        key = turn_dic(key)
        #검사를 할 범위 지정 
        for x in range(N*2):
            for y in range(N*2):
                #자물쇠에 열쇠를 끼워넣기 
                for i in range(M):
                    for j in range(M):
                        new_lock[i+x][j+y] +=key[i][j]
                if check(new_lock) == True:
                    return True
                #자물쇠에서 열쇠 빼기 
                for i in range(M):
                    for j in range(M):
                        new_lock[i+x][j+y] -=key[i][j]
    return False