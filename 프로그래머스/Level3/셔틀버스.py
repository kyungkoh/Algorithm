#0822 
#단순한 구현 문제 였는데, 
#시간을 분으로 바꿔서 푸는 걸 생각못하고, 조건문을 쉽게 찾아 내지 못해서 오래 걸린 문제다 
# 카카오 코테 일정이 나오고 나서 더 의욕이 없어진 듯 싶다..

def solution(n, t, m, timetable):
    answer = ''
    #크루 도착 시간 리스트
    crewtime = [int(t[:2])*60 + int(t[3:5]) for t in timetable]
    crewtime.sort()
    #버스 도착 시간 리스트
    bus_time = [9*60 + i*t for i in range(n)]
    
    i =0 # 버스에 탈 크루의 수 
    for tm in bus_time:
        cnt = 0 
        while cnt < m and i<len(crewtime) and crewtime[i]<=tm : 
            cnt+=1
            i+=1
        #버스에 자리가 남았을 경우 
        if cnt < m :
            answer = tm
        #자리가 없을 경우, 맨 마지막에 온 크루 보다 1분 일찍 도착한다 
        else: 
            answer = crewtime[i-1] -1
            
    ret = str(answer//60).zfill(2)+ ":" +str(answer%60).zfill(2)
    return ret