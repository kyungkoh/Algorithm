#0923
#백준 16953 BFS/DFS

from collections import deque

a,b = map(int,input().split())
dq = deque()
dq.append((a,1))
answer = -1

while dq:
    i, cnt = dq.popleft()
    if i == b:
        answer = cnt
        break
    
    if i*2<=b:
        dq.append((i*2,cnt+1))

    if int(str(i)+'1') <= b:
        dq.append((int(str(i)+'1'),cnt+1))

print(answer)