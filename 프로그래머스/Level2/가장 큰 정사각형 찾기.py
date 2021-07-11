#210711

def solution(board):
    answer = 0

    # 정사각형의 크기가 0과 1일때를 예외처리 
    for row in board: 
        if sum(row)==1:
            answer = 1
            break
        elif sum(row)==0:
            answer =0 
            break
    
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] and board[i-1][j] and board[i][j-1] and board[i-1][j-1]:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
                answer = max(answer,board[i][j])

    return answer**2