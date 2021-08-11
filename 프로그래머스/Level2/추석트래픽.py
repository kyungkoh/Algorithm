#0812 
#string, implementation
def get_time(time):
    hour = int(time[:2])*3600
    minute = int(time[3:5])*60
    sec = int(time[6:8])
    milsec = int(time[9:])
    
    total = (hour+minute+sec)*1000 + milsec
    
    return total 

def get_start_time(time, duration):
    d_time = duration[:-1]
    int_time = int(float(d_time)*1000)
    return get_time(time) - int_time +1

def solution(lines):
    answer = 0
    start_time = []
    end_time = []
    
    for time in lines: 
        t = time.split(" ")
        start_time.append(get_start_time(t[1],t[2]))
        end_time.append(get_time(t[1]))
    
    for i in range(len(lines)):
        cnt = 0
        cur_endtime = end_time[i]
        for j in range(i,len(lines)):
            if cur_endtime > start_time[j] - 1000:
                cnt+=1
                
        answer = max(answer,cnt)
        
    return answer