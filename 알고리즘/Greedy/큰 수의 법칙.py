#0805 
#실전 프로그래밍_실전 문제2

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))

answer = 0 

arr = arr.sort()
first = arr[0]
second = arr[1]

while True : 
    for i in range(k):
        if m == 0:
            break
        answer+=first
        m-=1
    if m==0:
        break
    answer+=second
    m-=1

print(answer)