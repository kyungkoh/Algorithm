#0805 
#실전 프로그래밍_예제 3-1

n = int(input())
count = 0 

coin_types = [500,100,50,10]

for coin in coin_types:
    count += (n//coin)
    n = n%coin

print(count)