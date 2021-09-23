#백준 14719
answer = 0 

h,w = map(int,input().split())
rain = list(map(int,input().split()))

for i in range(1,w-1):
    left = max(rain[:i])
    right = max(rain[i+1:])

    m = min(left,right)

    if m > rain[i]:
        answer += (m-rain[i])

print(answer)
