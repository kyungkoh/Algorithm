def solution(jobs):
    answer = 0
    start = 0
    length = len(jobs)
    jobs = sorted(jobs,key = lambda x:x[1])
    #print(jobs)
    
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0]<=start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            #해당 시점에 아직 작업이 들어오지 않았으면 시간을 더해준다 (1초씩)
            else:
                start+=1
        
    
    return answer//length