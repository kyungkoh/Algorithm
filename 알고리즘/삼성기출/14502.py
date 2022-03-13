#1010 

n,m = map(int,input().stript().split())

graph = []

for i in range(n): 
    L = list(map(int,input().strip().split()))
    graph.append(L)

dr = [-1,0,1,0]
dc = [0,1,0,-1]

max_v = 0 
