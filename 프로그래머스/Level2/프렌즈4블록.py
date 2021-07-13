#0713 
def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    def games(b):
        pops = 0
        flag = [i[:] for i in b]
    
        for i in range(1,n):
            for j in range(1,m):
                if board[i][j] == -1 : continue
                if board[i][j] == board[i-1][j] == board[i][j-1] == board[i-1][j-1]:
                    flag[i][j],flag[i-1][j],flag[i][j-1],flag[i-1][j-1] = 0,0,0,0
                
        #터진 블록 개수 세기 
        for i,v in enumerate(flag):
            cnt = v.count(0)
            pops += cnt
            flag[i] = [-1]*cnt + [a for a in v if a!=0]
            
        return flag,pops
    
    while True:
        board,pops = games(board)
        if pops == 0: return answer
        answer+=pops
            
    return answer