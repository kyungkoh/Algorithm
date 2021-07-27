
#0726 
#다익스트라 알고리즘 (heap 버전)

import heapq

INF = int(1e9)

def solution(N, road, K):
    answer = 0

    graph =[[] for _ in range(N+1)]
    
    #간선의 정보 입력
    for r in road:
        graph[r[0]].append((r[1],r[2]))
        graph[r[1]].append((r[0],r[2]))
        
    #최단거리 테이블 초기화 
    distance = [INF]*(N+1)
    
    #print(graph)
    
    q = []
    start = 1
    heapq.heappush(q,(0,start))
    distance [start] = 0 
    #큐가 비어있지 않다면 
    while q:
        dist,now = heapq.heappop(q)
        #현재 노드가 처리 된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #현재노드와 연결 되어 있는 다른 노드들 확인 
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    #print(distance)
    
    for i in range(1,N+1):
        if distance[i]<=K:
            answer+=1
            
    return answer