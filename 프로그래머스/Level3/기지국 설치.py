# 0925
#implementation

import math
def solution(n, stations, w):
    answer = 0

    distance = []
    
    for s in range(1,len(stations)):
        distance.append((stations[s]-w)-(stations[s-1]+w)-1)

    distance.append(stations[0]-w-1)
    distance.append(n-stations[-1]-w)
    
    print(distance)
    
    dd = (w*2)+1
    
    for d in distance:
        if d <=0:
            continue
        else:
            answer += (math.ceil(d/dd))
    return answer