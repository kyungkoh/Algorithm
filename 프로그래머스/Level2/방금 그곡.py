# 카카오 특유의 스트링 처리 문제 
# 그래도 쉽진 않다 ^^

def change(music_):
    music_ = music_.replace('C#','c')
    music_ = music_.replace('D#','d')
    music_ = music_.replace('F#','f')
    music_ = music_.replace('G#','g')
    music_ = music_.replace('A#','a')
    
    return music_

def cal_time (musicinfo_):
    s_time = musicinfo_[0]
    f_time = musicinfo_[1]
    
    hour = 1*(int(f_time.split(':')[0]) - int(s_time.split(':')[0]))
    
    if hour == 0 : 
        total = int(f_time.split(':')[1]) - int(s_time.split(':')[1])
    else: 
        total = (hour*60) + int(f_time.split(':')[1]) - int(s_time.split(':')[1])
    return total  

def solution(m, musicinfos):
    answer = []
    m = change(m)
        
    for idx, musicinfo in enumerate(musicinfos):
        musicinfo = change(musicinfo)
        musicinfo = musicinfo.split(',')
        time = cal_time(musicinfo)
        
        # 길이가 재생 시간보다 긴 경우
        if len(musicinfo[3]) >= time:
            melody = musicinfo[3][:time]
        else: 
            a = time // len(musicinfo[3])
            b = time % len(musicinfo[3])
            melody = a * musicinfo[3] + musicinfo[3][:b]
            
        if m in melody: 
            answer.append([idx,time,musicinfo[2]])
        
    if len(answer) !=0 : 
        answer = sorted(answer,key = lambda x: (-x[1],x[0]))
        return answer[0][2]
    else: 
        return "(None)"
        
            
        
    return time