#0810 
#binary search
def solution(n, times):
    answer = 0
    
    length = len(times)
    left = 1
    right = (length+1)*max(times) # 심사받는 최대 시간
    
    while left <= right:
        mid = (left+right)//2
        count = 0 
        for t in times: 
            count += mid // t
            #print(count)
        #print('=========')
        
        #n명을 심사 할 수 있는 경우 
        #심사관에게 주어진 시간을 줄여본다 
        if count >= n:
            answer = mid
            right = mid - 1
        
        elif count<n:
            left = mid+1
    
    return answer