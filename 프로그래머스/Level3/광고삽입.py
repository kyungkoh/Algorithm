#0829 
# 카카오 특유의 시간문자열 문제.. 
# 사실 거의 혼자 힘으로 풀지못했다. 이걸 어떻게 생각 해내지 ㅋㅋ 
# 누적 합과 약간의 슬라이딩 윈도우에 대해서 감을 익힐 수 있었다 카카오 코테까지 시간이 얼마남지 않아 좀 심적인 여유가 많지 않다 
# 사실 카카오 유형만 보면 되는게 아닌거 같은데 ㅋㅋ 어렵다 어려워 

def timetosec(s):
    total = 0 
    total = int(s[:2])*3600+ int(s[3:5])*60 + int(s[6:8])
    return total 

def sectotime(t):
    hour = t//3600
    t -= (hour*3600)
    min = t//60
    t -= (min*60)
    
    return f"{str(hour).zfill(2)}:{str(min).zfill(2)}:{str(t).zfill(2)}"

def solution(play_time, adv_time, logs):
    answer = 0
    
    play_sec = timetosec(play_time)
    adv_sec = timetosec(adv_time)
    
    total_time = [0]*(play_sec+1)
    
    
    for l in logs: 
        t_start , t_end = l.split('-')
        #시작시간, 끝나는 시간을 초로 변환
        start_sec = timetosec(t_start)
        end_sec = timetosec(t_end)
        #시작시간에는 시청자 수 +1, 끝나는 시간에는 시청자 수 -1
        total_time[start_sec]+=1
        total_time[end_sec]-=1

    #누적 합을 돌면 비어있는 시간의 시청자 수를 알 수 있음
    #[0,0,0,1,0,0,0,1,0...] => [0,0,0,1,1,1,1,2...]
    for i in range(1,play_sec+1):
        total_time[i] = total_time[i-1]+total_time[i]
    
    #누적 합을 한번더 돌면 시청 시간을 알 수 있음..?
    
    for i in range(1,play_sec+1):
        total_time[i] = total_time[i-1] + total_time[i]
        
    #0초에 광고를 시작했을 때 시청자 
    max_cnt = total_time[adv_sec]
    
    for start in range(1,play_sec):
        if start + adv_sec >= play_sec: 
            end = play_sec
        else:
            end = start+adv_sec
        
        if max_cnt < total_time[end] - total_time[start]:
            max_cnt = total_time[end]-total_time[start]
            answer  = start+1
            
    answer = sectotime(answer)
    
    return answer